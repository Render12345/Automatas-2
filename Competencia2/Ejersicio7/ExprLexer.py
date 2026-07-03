# Generated from ./Expr.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,5,36,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,
        0,1,0,1,1,1,1,5,1,18,8,1,10,1,12,1,21,9,1,1,2,4,2,24,8,2,11,2,12,
        2,25,1,3,1,3,1,4,4,4,31,8,4,11,4,12,4,32,1,4,1,4,0,0,5,1,1,3,2,5,
        3,7,4,9,5,1,0,4,4,0,36,36,65,90,95,95,97,122,5,0,36,36,48,57,65,
        90,95,95,97,122,1,0,48,57,3,0,9,10,13,13,32,32,38,0,1,1,0,0,0,0,
        3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,1,11,1,0,0,0,3,15,
        1,0,0,0,5,23,1,0,0,0,7,27,1,0,0,0,9,30,1,0,0,0,11,12,5,105,0,0,12,
        13,5,110,0,0,13,14,5,116,0,0,14,2,1,0,0,0,15,19,7,0,0,0,16,18,7,
        1,0,0,17,16,1,0,0,0,18,21,1,0,0,0,19,17,1,0,0,0,19,20,1,0,0,0,20,
        4,1,0,0,0,21,19,1,0,0,0,22,24,7,2,0,0,23,22,1,0,0,0,24,25,1,0,0,
        0,25,23,1,0,0,0,25,26,1,0,0,0,26,6,1,0,0,0,27,28,5,61,0,0,28,8,1,
        0,0,0,29,31,7,3,0,0,30,29,1,0,0,0,31,32,1,0,0,0,32,30,1,0,0,0,32,
        33,1,0,0,0,33,34,1,0,0,0,34,35,6,4,0,0,35,10,1,0,0,0,4,0,19,25,32,
        1,6,0,0
    ]

class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INT = 1
    ID = 2
    NUM = 3
    ASIG = 4
    WS = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "INT", "ID", "NUM", "ASIG", "WS" ]

    ruleNames = [ "INT", "ID", "NUM", "ASIG", "WS" ]

    grammarFileName = "Expr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


