.SUFFIXES: .java .class

JAVAC	= javac
JAVA	= java
SRC	= $(wildcard *.java)
CLASS	= $(SRC:.java=.class)
PROGRAM	= $(shell pwd)

all: $(CLASS)

test:;
	@echo 今回は make test は使用できません。make kadai1, make kadai2, make kadai3 で課題チェックが動くようMakefileを編集してください。

.java.class:
	$(JAVAC) $<

clean:;	\rm -f *.class
