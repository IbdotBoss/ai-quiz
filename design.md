# Design: AI test practice

## Brief

- **Subject.** A 50-minute computer-based in-class test for MOD004553 Artificial Intelligence at ARU. The tutor describes the questions as primarily descriptive, with no calculations. The practicals are Jupyter notebooks full of matplotlib and seaborn plots.
- **Audience.** Stage, revising on a phone and a laptop in short sessions.
- **The one job.** Get him explaining each idea in his own words, then show him which marking points his answer missed.
- **Material.** 372 questions drafted from the 12 lecture decks, 12 revision sheets. No past paper and no mock test yet.
- **Absent.** No logo, photos or illustrations. None are invented.
- This is a product surface used daily, so `product-surfaces.md` applies.

## Concept

Your revision is a plot from the practicals. The home page is a heatmap of what you know.

The week name in each row opens that week's page, with its notes, both question sets and a box for sending your own question to an assistant.

Signature: a table of weeks by question type where each square is coloured on the viridis colormap by the share of questions answered right. Each square is also the button that starts practice for that week. Squares never tried are hatched and say "new".

## References

- **matplotlib and seaborn output in the module's own notebooks.** Taken: viridis in ten steps, square annotated cells with light text on dark steps and dark text on light steps, a stepped colour key under the plot. Left out: axis ticks, the default DejaVu Sans face, figure borders.
- No live quiz products were surveyed. The reference is the subject's own visual vernacular.

## Tokens

```css
:root {
  --paper: #fff;
  --ink: #1b1424;     /* text, rules, primary button. A near black tinted toward viridis purple */
  --ink-2: #4b4357;   /* secondary text, 9.3:1 on paper */
  --hair: #dedbe4;    /* dividers */
  --tint: #f4f2f7;    /* the block that shows your own answer, and notes */
  --right: #18794e;   /* tick and the word Right, 5.4:1 */
  --wrong: #b3261e;   /* cross and the words Wrong and Missed, 6.5:1 */
  --focus: #3e4a89;   /* focus ring, viridis step 2 */
  --t-xs: .84rem; --t-s: .94rem; --t-m: 1.0625rem; --t-l: 1.375rem; --t-xl: 2.25rem;
  --r: 6px;
}
/* viridis, ten steps */
#440154 #482878 #3e4a89 #31688e #26828e #1f9e89 #35b779 #6ece58 #b5de2b #fde725
```

Spacing sits on a 4px base. Data is square with no radius. Controls have a 6px radius.

## Type

- **Atkinson Hyperlegible Next**, variable weight 200 to 800, SIL OFL. One family. It was drawn for legibility, and this page is mostly reading and typing paragraphs. Headings at 700 and 800, body at 400.
- Five text sizes. Heatmap numbers are 1.2rem at weight 800 so they count as large text for contrast. No letter-spacing changes.
- The face is embedded as base64 woff2, latin subset, so the file works offline.

## Assets

Type and rules only, plus a tick and a cross drawn as SVG paths. Nothing is missing from Stage.

## Motion

None.

## Refused

- **The PICS exam-paper look.** Stage asked for a new look, and this test is on a computer.
- **Notebook cells with an In and Out gutter.** Comp B. It leans on mono type for labels and makes the progress view a plain table.
- **Blueprint blue with a network diagram.** Comp C. The diagram is decoration and says nothing about progress.
- **A colour per week.** Colour has one job here, which is the score.
- **Dark mode, progress bars and stat tiles.**

The three comps are in `comps/index.html`.

## Overrides

- `ui-skills` bans gradients. The hatched "new" square uses a repeating gradient as a pattern, so the unstarted state does not rely on colour alone. The colour key is ten flat swatches.
- `ui-skills` assumes Tailwind and a component library. This is one static file with native inputs and a native `dialog`.
- `web-quality` asks each shipped colour scheme to pass. One scheme ships.
- Hallmark's linter asks for a tinted ground in place of pure white. White stays, because a matplotlib figure sits on white.
- Hallmark's stamp comment is left out. Hallmark did not build this page. Its linter ran on 16 Nov 2026 and every other finding was fixed.
- Viridis steps 3 and 4 give white text 4.3:1 and above only at large text size, which is why the numbers are 1.2rem bold.

## Stack

One static HTML file built by `build.py`, with questions, notes and the font inlined. No routes and no server data, and it opens by double-click offline.
