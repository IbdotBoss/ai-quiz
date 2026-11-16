"""Build index.html and docs/index.html from bank/*.json and notes/*.md.

Checks every question's shape and writes nothing if one fails.
Usage: python build.py
"""
import base64, glob, json, os, re, subprocess, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
errors, questions, seen_ids = [], [], set()
BANNED_STEM = ("in the lecture", "according to the slides", "is listed", "as discussed", "the slides")

for path in sorted(glob.glob(os.path.join(HERE, "bank", "*.json"))):
    name = os.path.basename(path)
    deck = name[:-5]
    for q in json.load(open(path, encoding="utf8")):
        qid = q.get("id", "?")
        problems = []
        need = ("id", "week", "topic", "type", "q", "source")
        need += ("model", "points") if q.get("type") == "explain" else ("options", "answer", "explain")
        problems += [f"missing {k}" for k in need if q.get(k) in ("", None, [])]
        if not problems:
            if qid in seen_ids:
                problems.append("duplicate id")
            if any(b in q["q"].lower() for b in BANNED_STEM):
                problems.append("stem refers to the lecture or slides")
            if q["type"] == "explain":
                if not 3 <= len(q["points"]) <= 5:
                    problems.append(f"{len(q['points'])} points")
            elif q["type"] in ("single", "multi"):
                n, a = len(q["options"]), q["answer"]
                if any((not isinstance(i, int)) or i < 0 or i >= n for i in a) or len(set(a)) != len(a):
                    problems.append("answer index out of range or repeated")
                if q["type"] == "single" and (len(a) != 1 or n != 4):
                    problems.append("single needs four options and one answer")
                if q["type"] == "multi" and (len(a) < 2 or not 4 <= n <= 6):
                    problems.append("multi needs four to six options and two or more answers")
                if len({" ".join(o.lower().split()) for o in q["options"]}) != n:
                    problems.append("duplicate options")
            else:
                problems.append("bad type")
        if problems:
            errors += [f"{name} {qid}: {p}" for p in problems]
            continue
        seen_ids.add(qid)
        q["flag"] = q.get("flag", "") or ""
        q["deck"] = deck
        questions.append(q)

if errors:
    print("\n".join(errors))
    sys.exit(f"{len(errors)} problem(s); nothing written")

notes = []
for path in sorted(glob.glob(os.path.join(HERE, "notes", "*.md"))):
    html = subprocess.run(["pandoc", "-f", "gfm", "-t", "html", path], capture_output=True, check=True).stdout.decode("utf8")
    notes.append({"deck": os.path.basename(path)[:-3], "html": html})

tpl = open(os.path.join(HERE, "template.html"), encoding="utf8").read()
assert "/*FONT*/" in tpl and "/*DATA*/" in tpl
font = open(os.path.join(HERE, "fonts", "AtkinsonHyperlegibleNext.woff2"), "rb").read()
tpl = tpl.replace("/*FONT*/", base64.b64encode(font).decode())
data = json.dumps({"questions": questions, "notes": notes}, ensure_ascii=False).replace("</", "<\\/")
out = tpl.replace("/*DATA*/", data)

# docs/index.html is what GitHub Pages serves. index.html is the same file for opening locally.
for path in (os.path.join(HERE, "docs", "index.html"), os.path.join(HERE, "index.html")):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf8").write(out)

c = Counter((q["deck"], q["type"]) for q in questions)
for d in sorted({q["deck"] for q in questions}):
    print(f"{d:5} {c[(d,'single')]:>3} single  {c[(d,'multi')]:>3} multi  {c[(d,'explain')]:>3} explain")
print(len(questions), "questions,", sum(1 for q in questions if q["flag"]), "flagged,", len(notes), "note files")
