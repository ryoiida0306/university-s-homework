MAIN = Main.java
EXAS = example/*.java
LEAS = league/*.java
OTHS = othello6/*.java

MAINC = Main.class
EXASC = example/*.class
LEASC = league/*.class
OTHSC = othello6/*.class

JAVAC = javac
RM = rm

all: $(MAINC)

$(MAINC):
	$(JAVAC) $(EXAS) 
	$(JAVAC) $(LEAS)
	$(JAVAC) $(OTHS)
	$(JAVAC) $(MAIN)

clean: 
	$(RM) *.class

