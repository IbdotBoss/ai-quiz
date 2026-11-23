# AI test practice

Practice questions and revision notes for the MOD004553 Artificial Intelligence in-class test at ARU.

**Live:** https://ibdotboss.github.io/ai-quiz/

## What it does

- 118 questions for Weeks 1 to 11, 40 written and 78 multiple choice. Each week has its Test focus written question, about two more written questions and about six multiple choice. All 30 questions from the tutor's mock are kept.
- A written-answer question gives you a box to type in. You then see a model answer and tick the marking points your answer made. The page labels the points whose key terms appear in your answer, but it ticks nothing: only your own ticks count towards the mark.
- The home page lists what to do in order: revision notes, written answers, multiple choice, questions to redo, a mixed set and a timed paper. Written answers and multiple choice each have Study and Test. Study shows every question on one page with its answer.
- Below the list is a heatmap. Each square shows the share of that week's questions you have right, and starts a short set from that week.
- Each week has its own page with its notes. The notes explain each idea, give an example and name what it is confused with. A box under the notes sends your own question to an assistant.
- Test focus is one broad written question per week, 11 in all: the 10 from the tutor's mock and one for Week 11. Its Test gives 4 of them in 40 minutes, weakest first.
- A timed paper follows the real test format: 4 written and 10 multiple choice questions in 50 minutes.
- The tutor's mock test has its own Study and Test. Written questions 1 to 3 use the tutor's sample answers. Questions 4 to 10 had none, so their model answers were written from the slides and carry a note.
- Each question can open in Claude, ChatGPT, Perplexity or Gemini with the question and your answer filled in.
- Progress is saved in your browser. Nothing is sent anywhere.

## How the questions were made

The slide text was extracted from the 13 decks. Questions were drafted from that text only, then every answer key and marking point was checked against the slides by a second read. Where a question leans on standard textbook knowledge the slides do not state, it carries a note.

A second pass reworded unclear stems, options, explanations and notes against the house writing rules. The answer keys were compared with the first version by script, and each reworded right answer was read again.

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
