# Guide for Co-Authors

You can do everything on the GitHub website. Nothing you do can break the manuscript:
your edits go to Cass as a suggestion, and Cass reviews them before they become part of the main version.

## Where things are

| What | Where | Do you edit it? |
|---|---|---|
| The manuscript | [`manuscript/manuscript.md`](manuscript/manuscript.md) | **Yes**, this is where you write |
| Tables | [`tables/`](tables/) | No, Cass maintains these |
| Figures | [`figures/`](figures/) | No, Cass maintains these |
| GenAI use logs | [`genai-logs/`](genai-logs/) | You upload your own logs here |

## How to make an edit

1. Open [`manuscript/manuscript.md`](manuscript/manuscript.md).
2. Click the **pencil icon** (top right of the file) to edit.
3. Type your text under the right heading. Leave the headings as they are.
4. Click the green **Commit changes...** button.
5. Write a short note of what you changed, for example `Add limitations paragraph to Discussion`.
6. Choose **Create a new branch for this commit and start a pull request**, then click **Propose changes**.
7. On the next page click **Create pull request**. Done. Cass will review it.

**Making more changes to the same suggestion:** open your pull request, click the **Files changed** tab,
click the **...** menu next to the file name, and choose **Edit file**. Your new commit is added to the same pull request.

**Questions instead of edits:** in your pull request, click the **+** next to any line to leave a comment.

## How to upload a GenAI use log

If you used GenAI while drafting, run the `genai-log` skill at the end of that chat and download the log file it makes.
File names follow `genai-log-YYYY-MM-DD-<initials>-<topic>.md`, for example `genai-log-2026-10-22-cd-discussion-draft.md`.

1. Open the [`genai-logs`](genai-logs/) folder. Your upload lands in whichever folder you are viewing.
2. Click **Add file**, then **Upload files**, and drag your log file in.
3. Choose **Create a new branch for this commit and start a pull request**, then **Propose changes**, then **Create pull request**.

**To put the log in the same pull request as your manuscript edits:** before step 1, use the branch menu
at the top left of the file list to switch to your own branch (it has a name like `patch-1`).

## One habit that helps a lot

**Start each new sentence on its own line.** It still shows as a normal paragraph.
Leave a blank line between paragraphs.
This lets Cass see exactly which sentence you changed instead of a whole highlighted paragraph.

```markdown
First sentence of paragraph 1.
Second sentence of paragraph 1.

First sentence of paragraph 2.
```

One catch: a line that starts with `#`, `- `, `* `, `>` or a number and period like `1. `
turns into a heading, bullet, quote or numbered item.
If a sentence has to start that way, put a backslash before it, for example `2024\. was the year`.

## Copy and paste these

Point to a table (change the number in both places):

```markdown
(see [Table 1](../tables/table-1.md))
```

Show a figure (put it on its own line, change the number in both places):

```markdown
![Figure 1](../figures/figure-1.svg)
```

Keep the `../` at the start. It tells GitHub to look one folder up from the manuscript.
Ask Cass for the exact file name of a new table or figure.

## Formatting cheat sheet

| You type | You get |
|---|---|
| `**text**` | **bold** |
| `*text*` | *italic* |
| `***text***` | ***bold and italic*** |
| `[label](https://example.com)` | a link |
| `- item` at the start of a line | a bullet point |
| `1. item` at the start of a line | a numbered item |

In the GitHub editor, **Ctrl/Cmd + B** makes bold and **Ctrl/Cmd + I** makes italic.
Click the **Preview** tab at the top of the editor to check how it looks before committing.

## Citations (APA 7)

- In the text: Author (Year) or (Author, Year), with a page number for direct quotes: (Author, Year, p. 10).
- Add every source you cite to the **References** section at the end of the manuscript.
