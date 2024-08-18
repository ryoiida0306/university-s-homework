.SUFFIXES: .java .class

JAVAC	= javac
JAVA	= java
SRC	= $(wildcard *.java)
CLASS	= $(SRC:.java=.class)
PROGRAM	= $(shell pwd)
MAIN	= TextToUpperTester

all: $(CLASS)

test: $(CLASS)
	- mv foobar.txt foobar_bak.txt
	echo "testing data" > foobar.txt
	$(JAVA) $(MAIN)
	rm -f foobar.txt
	$(JAVA) $(MAIN)
	- mv foobar_bak.txt foobar.txt

$(CLASS): $(SRC)

.java.class:
	$(JAVAC) $<

clean:;	\rm -f *.class

