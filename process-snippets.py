#!/usr/bin/env python3

import fileinput,re
from pygments import highlight
from pygments.lexers.dotnet import FSharpLexer
from pygments.formatters import LatexFormatter

flag=False
snippet=""

for line in fileinput.input():
    if "%% PYGMENTS STYLE INSERTED HERE AUTOMATICALLY %%" in line:
        line=LatexFormatter(style="staroffice").get_style_defs()
    if "\\nwendcode" in line:
        flag=False
    if re.match(r'^\\LA{}',line):
        flag=False
        print(line.rstrip())
    if flag:
        snippet+=line
        if re.match(r'^\\LA{}',line):
            flag=True
    else:
        if snippet != "":
            snippet=highlight(snippet,FSharpLexer(),LatexFormatter())
            slines=snippet.split("\n")
            for sl in slines:
#                if "Verbatim" in sl:
#                    if "begin" in sl:
#                        print("\\begin{center}")
#                    if "end" in sl:
#                        print("\\end{center}")
#                elif "PYZbs" in sl:
                if "PYZbs" in sl:
                    out=re.sub("{\\\PYZbs{}\\\PYZbs{}}","{\\\PYZbs{}}",sl)
                    # FIXME: Should the bit between brackets remove the \PY{err}?
                    out=re.sub("\\{\\\PYZbs\\{\\}\\}\\\PY\\{l\\+s\\}\\{\\\PYZob\\{\\}","{\\\PYZob{}",out)
                    out=re.sub("\\{\\\PYZbs\\{\\}\\}\\\PY\\{l\\+s\\}\\{\\\PYZcb\\{\\}","{\\\PYZcb{}",out)
                    print(out)
                else:
                    print(sl)
            snippet=""
        else:
            print(re.sub(r'}%$',"}",line.rstrip()))
    if "\\nwbegincode" in line:
        flag=True
