# AI test practice

Practice questions and revision notes for the MOD004553 Artificial Intelligence in-class test at ARU.

**Live:** https://ibdotboss.github.io/ai-quiz/

## What it does

- 372 questions drafted from the lecture slides for Weeks 1 to 10. 266 are multiple choice and 106 are written-answer questions.
- A written-answer question gives you a box to type in. You then see a model answer and tick the marking points your answer made.
- The home page is a heatmap. Each square shows the share of that week's questions you have right, and starts a short set from that week.
- Each week has its own page with its notes and a box for sending your own question to an assistant.
- A timed paper gives 8 written-answer questions in 50 minutes. The real format is not published yet, so this is a guess.
- Each question can open in Claude, ChatGPT, Perplexity or Gemini with the question and your answer filled in.
- Progress is saved in your browser. Nothing is sent anywhere.

## How the questions were made

The slide text was extracted from the 12 decks. Questions were drafted from that text only, then every answer key and marking point was checked against the slides by a second read. Where a question leans on standard textbook knowledge the slides do not state, it carries a note.

The wrong options of single-answer questions, the explanations and the revision notes were sampled, not all read.

## Build

```bash
python fonts/fetch.py
```

```bash
python build.py
```

`build.py` checks every question and writes nothing if one fails. It needs `pandoc` for the notes. Output goes to `docs/index.html`, which GitHub Pages serves.

## Layout

- `bank/` one JSON file per lecture deck
- `notes/` one revision sheet per deck
- `template.html` the app
- `design.md` the design system and the reasons behind it

Created by [Ibrahim Uthman](https://www.ibrahimuthman.me/).
