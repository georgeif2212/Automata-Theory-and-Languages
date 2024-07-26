# Generated from /content/drive/MyDrive/ColabNotebooks/Automatas/Practica3/Ejemplo.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,9,57,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,4,4,29,
        8,4,11,4,12,4,30,1,4,1,4,1,5,1,5,1,6,4,6,38,8,6,11,6,12,6,39,1,7,
        1,7,5,7,44,8,7,10,7,12,7,47,9,7,1,7,1,7,1,8,1,8,5,8,53,8,8,10,8,
        12,8,56,9,8,0,0,9,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,1,0,5,
        3,0,9,10,13,13,32,32,1,0,48,57,4,0,32,32,48,58,65,90,97,122,2,0,
        65,90,97,122,3,0,48,57,65,90,97,122,60,0,1,1,0,0,0,0,3,1,0,0,0,0,
        5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,
        1,0,0,0,0,17,1,0,0,0,1,19,1,0,0,0,3,21,1,0,0,0,5,23,1,0,0,0,7,25,
        1,0,0,0,9,28,1,0,0,0,11,34,1,0,0,0,13,37,1,0,0,0,15,41,1,0,0,0,17,
        50,1,0,0,0,19,20,5,59,0,0,20,2,1,0,0,0,21,22,5,61,0,0,22,4,1,0,0,
        0,23,24,5,40,0,0,24,6,1,0,0,0,25,26,5,41,0,0,26,8,1,0,0,0,27,29,
        7,0,0,0,28,27,1,0,0,0,29,30,1,0,0,0,30,28,1,0,0,0,30,31,1,0,0,0,
        31,32,1,0,0,0,32,33,6,4,0,0,33,10,1,0,0,0,34,35,2,42,43,0,35,12,
        1,0,0,0,36,38,7,1,0,0,37,36,1,0,0,0,38,39,1,0,0,0,39,37,1,0,0,0,
        39,40,1,0,0,0,40,14,1,0,0,0,41,45,5,34,0,0,42,44,7,2,0,0,43,42,1,
        0,0,0,44,47,1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,48,1,0,0,0,47,
        45,1,0,0,0,48,49,5,34,0,0,49,16,1,0,0,0,50,54,7,3,0,0,51,53,7,4,
        0,0,52,51,1,0,0,0,53,56,1,0,0,0,54,52,1,0,0,0,54,55,1,0,0,0,55,18,
        1,0,0,0,56,54,1,0,0,0,5,0,30,39,45,54,1,6,0,0
    ]

class EjemploLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    ESPACIOS = 5
    OPERADORES = 6
    NUMERO = 7
    STRINGS = 8
    VARIABLE = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'='", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "ESPACIOS", "OPERADORES", "NUMERO", "STRINGS", "VARIABLE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "ESPACIOS", "OPERADORES", 
                  "NUMERO", "STRINGS", "VARIABLE" ]

    grammarFileName = "Ejemplo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


