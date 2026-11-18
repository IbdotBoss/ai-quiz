# AI test practice

Practice questions and revision notes for the MOD004553 Artificial Intelligence in-class test at ARU.

**Live:** https://ibdotboss.github.io/ai-quiz/

## What it does

- 372 questions drafted from the lecture slides for Weeks 1 to 10. 266 are multiple choice and 106 are written-answer questions.
- A written-answer question gives you a box to type in. You then see a model answer and tick the marking points your answer made. The page ticks the points whose key terms it finds in your answer, and you correct its ticks.
- The home page lists what to do in order: revision notes, written answers, multiple choice, questions to redo, a mixed set and a timed paper. Written answers and multiple choice each have Study and Test. Study shows every question on one page with its answer.
- Below the list is a heatmap. Each square shows the share of that week's questions you have right, and starts a short set from that week.
- Each week has its own page with its notes. The notes explain each idea, give an example and name what it is confused with. A box under the notes sends your own question to an assistant.
- A timed paper gives 8 written-answer questions in 50 minutes. The real format is not published yet, so this is a guess.
- Each question can open in Claude, ChatGPT, Perplexity or Gemini with the question and your answer filled in.
- Progress is saved in your browser. Nothing is sent anywhere.

## Core set

The home page switches between the full bank and a core set of 193 questions, which is one multiple choice and one written question on each main topic. `select_core.py` tags the core questions and can be run again after the bank changes.

## How the questions were made

The slide text was extracted from the 12 decks. Questions were drafted from that text only, then every answer key and marking point was checked against the slides by a second read. Where a question leans on standard textbook knowledge the slides do not state, it carries a note.

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
