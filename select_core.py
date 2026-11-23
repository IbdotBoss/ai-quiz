"""Tag the core set in bank/*.json. Repeatable: python select_core.py

Rule: for each topic in each deck, the first written-answer question and the first multiple choice
question are core, and so is every question from the tutor's mock test. Topics in SKIP add detail a descriptive test is unlikely to ask, so they stay out.
"""
import glob, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
SKIP = {
    "Multiple intelligences", "Value of AI in research", "Scientific method in AI", "AI research pipeline",
    "Uses of regression", "Types of machine learning", "Unsupervised learning applications",
    "Uses of genetic algorithms", "Biological inspiration", "Network structure", "Images and channels",
    "YOLO backbone", "YOLO preprocessing", "Classification algorithms", "Segmentation uses", "NLP applications",
}
# Written questions the first-per-topic rule leaves out but a descriptive test is likely to ask. Added by hand.
ALSO = {"w01a-022", "w02-032", "w03-026", "w06-030"}
total = [0, 0]
for path in sorted(glob.glob(os.path.join(HERE, "bank", "*.json"))):
    qs = json.load(open(path, encoding="utf8"))
    seen = set()
    n = [0, 0]
    for q in qs:
        kind = q["type"] == "explain"
        key = (q["topic"], kind)
        q["core"] = q.get("mock", False) or q["id"] in ALSO or (q["topic"] not in SKIP and key not in seen)
        if q["topic"] not in SKIP:
            seen.add(key)
        n[kind] += q["core"]
    json.dump(qs, open(path, "w", encoding="utf8"), ensure_ascii=False, indent=1)
    total[0] += n[0]; total[1] += n[1]
    print(f"{os.path.basename(path)[:-5]:5} {n[0]:>3} multiple choice  {n[1]:>3} written  of {len(qs)}")
print("core:", total[0], "multiple choice,", total[1], "written,", sum(total), "in all")
