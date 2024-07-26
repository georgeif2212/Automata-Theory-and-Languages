# Generated from /content/drive/MyDrive/ColabNotebooks/Automatas/Practica3/Ejemplo.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,9,56,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,5,0,
        14,8,0,10,0,12,0,17,9,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,
        28,8,1,1,2,1,2,1,2,1,2,1,2,1,2,5,2,36,8,2,10,2,12,2,39,9,2,1,3,1,
        3,1,3,1,3,1,3,1,3,3,3,47,8,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,0,1,
        4,6,0,2,4,6,8,10,0,1,1,0,7,9,54,0,15,1,0,0,0,2,27,1,0,0,0,4,29,1,
        0,0,0,6,46,1,0,0,0,8,48,1,0,0,0,10,53,1,0,0,0,12,14,3,2,1,0,13,12,
        1,0,0,0,14,17,1,0,0,0,15,13,1,0,0,0,15,16,1,0,0,0,16,1,1,0,0,0,17,
        15,1,0,0,0,18,19,3,4,2,0,19,20,5,1,0,0,20,28,1,0,0,0,21,22,3,6,3,
        0,22,23,5,1,0,0,23,28,1,0,0,0,24,25,3,8,4,0,25,26,5,1,0,0,26,28,
        1,0,0,0,27,18,1,0,0,0,27,21,1,0,0,0,27,24,1,0,0,0,28,3,1,0,0,0,29,
        30,6,2,-1,0,30,31,5,7,0,0,31,37,1,0,0,0,32,33,10,2,0,0,33,34,5,6,
        0,0,34,36,3,4,2,3,35,32,1,0,0,0,36,39,1,0,0,0,37,35,1,0,0,0,37,38,
        1,0,0,0,38,5,1,0,0,0,39,37,1,0,0,0,40,41,5,9,0,0,41,42,5,2,0,0,42,
        47,5,7,0,0,43,44,5,9,0,0,44,45,5,2,0,0,45,47,5,9,0,0,46,40,1,0,0,
        0,46,43,1,0,0,0,47,7,1,0,0,0,48,49,5,9,0,0,49,50,5,3,0,0,50,51,3,
        10,5,0,51,52,5,4,0,0,52,9,1,0,0,0,53,54,7,0,0,0,54,11,1,0,0,0,4,
        15,27,37,46
    ]

class EjemploParser ( Parser ):

    grammarFileName = "Ejemplo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'='", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ESPACIOS", "OPERADORES", "NUMERO", "STRINGS", 
                      "VARIABLE" ]

    RULE_programa = 0
    RULE_sentencia = 1
    RULE_expresion = 2
    RULE_asignacion = 3
    RULE_funcion = 4
    RULE_argumentos = 5

    ruleNames =  [ "programa", "sentencia", "expresion", "asignacion", "funcion", 
                   "argumentos" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    ESPACIOS=5
    OPERADORES=6
    NUMERO=7
    STRINGS=8
    VARIABLE=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EjemploParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(EjemploParser.SentenciaContext,i)


        def getRuleIndex(self):
            return EjemploParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = EjemploParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7 or _la==9:
                self.state = 12
                self.sentencia()
                self.state = 17
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(EjemploParser.ExpresionContext,0)


        def asignacion(self):
            return self.getTypedRuleContext(EjemploParser.AsignacionContext,0)


        def funcion(self):
            return self.getTypedRuleContext(EjemploParser.FuncionContext,0)


        def getRuleIndex(self):
            return EjemploParser.RULE_sentencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia" ):
                listener.enterSentencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia" ):
                listener.exitSentencia(self)




    def sentencia(self):

        localctx = EjemploParser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentencia)
        try:
            self.state = 27
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                self.expresion(0)
                self.state = 19
                self.match(EjemploParser.T__0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.asignacion()
                self.state = 22
                self.match(EjemploParser.T__0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 24
                self.funcion()
                self.state = 25
                self.match(EjemploParser.T__0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMERO(self):
            return self.getToken(EjemploParser.NUMERO, 0)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EjemploParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(EjemploParser.ExpresionContext,i)


        def OPERADORES(self):
            return self.getToken(EjemploParser.OPERADORES, 0)

        def getRuleIndex(self):
            return EjemploParser.RULE_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion" ):
                listener.enterExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion" ):
                listener.exitExpresion(self)



    def expresion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EjemploParser.ExpresionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expresion, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(EjemploParser.NUMERO)
            self._ctx.stop = self._input.LT(-1)
            self.state = 37
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EjemploParser.ExpresionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                    self.state = 32
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 33
                    self.match(EjemploParser.OPERADORES)
                    self.state = 34
                    self.expresion(3) 
                self.state = 39
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self, i:int=None):
            if i is None:
                return self.getTokens(EjemploParser.VARIABLE)
            else:
                return self.getToken(EjemploParser.VARIABLE, i)

        def NUMERO(self):
            return self.getToken(EjemploParser.NUMERO, 0)

        def getRuleIndex(self):
            return EjemploParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)




    def asignacion(self):

        localctx = EjemploParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_asignacion)
        try:
            self.state = 46
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.match(EjemploParser.VARIABLE)
                self.state = 41
                self.match(EjemploParser.T__1)
                self.state = 42
                self.match(EjemploParser.NUMERO)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.match(EjemploParser.VARIABLE)
                self.state = 44
                self.match(EjemploParser.T__1)
                self.state = 45
                self.match(EjemploParser.VARIABLE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(EjemploParser.VARIABLE, 0)

        def argumentos(self):
            return self.getTypedRuleContext(EjemploParser.ArgumentosContext,0)


        def getRuleIndex(self):
            return EjemploParser.RULE_funcion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncion" ):
                listener.enterFuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncion" ):
                listener.exitFuncion(self)




    def funcion(self):

        localctx = EjemploParser.FuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_funcion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(EjemploParser.VARIABLE)
            self.state = 49
            self.match(EjemploParser.T__2)
            self.state = 50
            self.argumentos()
            self.state = 51
            self.match(EjemploParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMERO(self):
            return self.getToken(EjemploParser.NUMERO, 0)

        def STRINGS(self):
            return self.getToken(EjemploParser.STRINGS, 0)

        def VARIABLE(self):
            return self.getToken(EjemploParser.VARIABLE, 0)

        def getRuleIndex(self):
            return EjemploParser.RULE_argumentos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentos" ):
                listener.enterArgumentos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentos" ):
                listener.exitArgumentos(self)




    def argumentos(self):

        localctx = EjemploParser.ArgumentosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_argumentos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 896) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expresion_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expresion_sempred(self, localctx:ExpresionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




