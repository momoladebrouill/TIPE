all:
	$(RM) logs.log
	pdflatex MCOT.latex >> /dev/null
	rm -f *.aux *.pytxcode
	mv MCOT.log logs.log
clean:
	rm -f *.aux *.pytxcode *.log *.toc *.out *.bbl *.blg *.pyg *.pytxmcr *.pytxpyg *.pytxcode *.pytxmcr *.pytxpyg *.pytxcode

