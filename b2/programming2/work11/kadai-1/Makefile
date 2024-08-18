.SUFFIXES: .java .class

JAVAC	= javac
JAVA	= java
SRC	= $(wildcard *.java)
CLASS	= $(SRC:.java=.class)
PROGRAM	= $(shell pwd)
MAIN	= FiboRec FiboDP

all: $(CLASS)

test: $(CLASS)
	$(JAVA) FiboRec 40
	$(JAVA) FiboDP 40

$(CLASS): $(SRC)

.java.class:
	$(JAVAC) $<

clean:;	\rm -f *.class

