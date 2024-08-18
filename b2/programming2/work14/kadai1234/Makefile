.SUFFIXES: .java .class

JAVAC	= javac
JAVA	= java
SRC	= $(wildcard *.java)
CLASS	= $(SRC:.java=.class)
PROGRAM	= $(shell pwd)

all: $(CLASS)

test:;
	@echo 今回は make test は使用できません
	@echo 初期のテストにはkada1から4をターゲットとする規則を用いてください
	@echo 10問の例題についての検証は自身で工夫して必ず行い報告すること
	@echo シェルスクリプトやMakefileの独自の規則を用いて良い

kadai1: WUGraph.class LoadPrintTester.class
	java LoadPrintTester wugraph/wug0.txt

kadai2: WUGraph.class EdgeSortTester.class
	java EdgeSortTester wugraph/wug0.txt

kadai3: UnionFind.class UnionFindTester.class
	java UnionFindTester

kadai4: UnionFind.class WUGraph.class MSTTester.class
	java MSTTester wugraph/wug0.txt


.java.class:
	$(JAVAC) $<

clean:;	\rm -f *.class
