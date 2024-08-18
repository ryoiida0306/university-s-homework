.SUFFIXES: .java .class

JAVAC	= javac
JAVA	= java
SRC	= $(wildcard *.java)
CLASS	= $(SRC:.java=.class)
PROGRAM	= $(shell pwd)
MAIN	= RevPolishNotationCalc

all: $(CLASS)

test: $(CLASS)
	@echo "8 7 6 + * = ? (answer=104)"
	@echo "8 7 6 + *" | $(JAVA) $(MAIN)
	@echo "9 8 2 / - = ? (answer=5)"
	@echo "9 8 2 / -" | $(JAVA) $(MAIN)
	@echo "3 4 + 5 4 2 / - * = ? (answer=21)"
	@echo "3 4 + 5 4 2 / - *" | $(JAVA) $(MAIN)

$(CLASS): $(SRC)

.java.class:
	$(JAVAC) $<

clean:;	\rm -f *.class

