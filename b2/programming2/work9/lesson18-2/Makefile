.SUFFIXES: .java .class

JAVAC	= javac
JAVA	= java
SRC	= $(wildcard *.java)
CLASS	= $(SRC:.java=.class)
PROGRAM	= $(shell pwd)

all: $(CLASS)

test: $(CLASS)
	$(JAVA) FindFile1 main FindFile1.java 
	$(JAVA) FindFile1 FindFile1 FindFile1.java 
	$(JAVA) FindFile1 TekitonaMojiretsu FindFile1.java 

$(CLASS): $(SRC)

.java.class:
	$(JAVAC) $<

clean:;	\rm -f *.class
