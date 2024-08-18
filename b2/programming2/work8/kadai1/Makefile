.SUFFIXES: .java .class

JAVAC	= javac
JAVA	= java
SRC	= $(wildcard *.java)
CLASS	= $(SRC:.java=.class)
PROGRAM	= $(shell pwd)

all: $(CLASS)

test: $(CLASS)
# cat を自動入力
	echo cat | $(JAVA) DictionaryTester 
# 猫 を自動入力
	echo 猫 | $(JAVA) DictionaryTester 


$(CLASS): $(SRC)

.java.class:
	$(JAVAC) $<

clean:;	\rm -f *.class
