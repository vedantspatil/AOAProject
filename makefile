JFLAGS = -g
JC = javac

.SUFFIXES: .java .class

.java.class: $(JC) $(JFLAGS) $*.java

CLASSES = \
    STRAT1.java \
    STRAT2.java \
    STRAT3.java \
    STRAT4.java

default: classes
classes: $(CLASSES:.java=.class)

clean: $(RM) *.class

run 1: java STRAT1

run 2: java STRAT2

run 3: java STRAT3

run 4: java STRAT4