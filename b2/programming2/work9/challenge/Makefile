.SUFFIXES: .java .class

JAVAC	= javac
JAVA	= java
SRC	= $(wildcard *.java)
CLASS	= $(SRC:.java=.class)
PROGRAM	= $(shell pwd)

all: $(CLASS)

test: $(CLASS)
	@echo Javaを検索
	$(JAVA) SearchWordRecursive ./ Java
	@echo Microsoftを検索
	$(JAVA) SearchWordRecursive ./ Microsoft

$(CLASS): $(SRC)

.java.class:
	$(JAVAC) $<

clean:;	\rm -f *.class
