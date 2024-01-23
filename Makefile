SHELL=/usr/bin/env bash

all: build doc

doc:
	noweave -x -delay Program.nw > Program.tex.tmp
	./process-snippets.py < Program.tex.tmp > Program.tex
	rm Program.tex.tmp
	xelatex --shell-escape Program; xelatex --shell-escape Program

build:
	notangle -RProgram.fs Program.nw > Program.fs

run: build
	dotnet run

clean:
	rm -f *.fs *.tex *.aux *.log *.pdf *.lot *.lof *.toc *.pyg *.tmp
	rm -rf bin
