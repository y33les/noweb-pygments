# Highlighting code chunks with Pygments in noweb documents

[noweb](https://www.cs.tufts.edu/~nr/noweb/) is a very cool literate programming tool.  Unfortunately, it's not easy to get noweb to play nicely with the Pygments syntax highlighter.  This repo includes an example document, `Program.nw`, a `Makefile` and a Python script, `process-snippets.py`, which manage to just about torture the document into complying.  It ain't pretty, but it (or at least this example) works.

You'll need Python3 with the `pygments` package installed, as well as a working LaTeX distribution.  In this example, we're using XeTeX; I haven't tried it with vanilla LaTeX yet, so YMMV.  To be honest, YMMV in general &ndash; this is a pretty ugly hack.

I've included the results of building this demo document in `Program.tex` and `Program.pdf`, for reference.
