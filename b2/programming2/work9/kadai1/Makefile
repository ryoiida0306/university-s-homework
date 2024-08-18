.SUFFIXES: .java .class

JAVAC	= javac
JAVA	= java
SRC	= $(wildcard *.java)
CLASS	= $(SRC:.java=.class)
PROGRAM	= $(shell pwd)

all: $(CLASS)

test: $(CLASS)
	$(JAVA) FileCopy sample_utf8.txt sample_utf8-copy.txt
	diff sample_utf8.txt sample_utf8-copy.txt
	$(JAVA) FileCopy sample_sjis.txt sample_sjis-copy.txt
	diff sample_sjis.txt sample_sjis-copy.txt
	$(JAVA) FileCopy sample.jpg sample-copy.jpg
	diff sample.jpg sample-copy.jpg

$(CLASS): $(SRC)

.java.class:
	$(JAVAC) $<

clean:;	\rm -f *.class
