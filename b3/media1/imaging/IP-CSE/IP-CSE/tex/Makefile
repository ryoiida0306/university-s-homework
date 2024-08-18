LATEX		= platex
SRCTEX		= main.tex
DVI = main.dvi
SRC		= ${SRCTEX:.tex=}
PDF		= ${SRCTEX:.tex=.pdf}
DVIPDF		= dvipdfmx
VIEWER		= acroread

all: ${PDF}

view: ${PDF}
	${VIEWER} ${PDF}

${PDF}: ${SRCTEX}
	${LATEX} ${SRC}
	${DVIPDF} ${DVI}

clean:
	\rm -f ${PDF} *.dvi *.aux *.log *~
