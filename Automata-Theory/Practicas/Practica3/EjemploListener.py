# Generated from /content/drive/MyDrive/ColabNotebooks/Automatas/Practica3/Ejemplo.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .EjemploParser import EjemploParser
else:
    from EjemploParser import EjemploParser

# This class defines a complete listener for a parse tree produced by EjemploParser.
class EjemploListener(ParseTreeListener):

    # Enter a parse tree produced by EjemploParser#programa.
    def enterPrograma(self, ctx:EjemploParser.ProgramaContext):
        pass

    # Exit a parse tree produced by EjemploParser#programa.
    def exitPrograma(self, ctx:EjemploParser.ProgramaContext):
        pass


    # Enter a parse tree produced by EjemploParser#sentencia.
    def enterSentencia(self, ctx:EjemploParser.SentenciaContext):
        pass

    # Exit a parse tree produced by EjemploParser#sentencia.
    def exitSentencia(self, ctx:EjemploParser.SentenciaContext):
        pass


    # Enter a parse tree produced by EjemploParser#expresion.
    def enterExpresion(self, ctx:EjemploParser.ExpresionContext):
        pass

    # Exit a parse tree produced by EjemploParser#expresion.
    def exitExpresion(self, ctx:EjemploParser.ExpresionContext):
        pass


    # Enter a parse tree produced by EjemploParser#asignacion.
    def enterAsignacion(self, ctx:EjemploParser.AsignacionContext):
        pass

    # Exit a parse tree produced by EjemploParser#asignacion.
    def exitAsignacion(self, ctx:EjemploParser.AsignacionContext):
        pass


    # Enter a parse tree produced by EjemploParser#funcion.
    def enterFuncion(self, ctx:EjemploParser.FuncionContext):
        pass

    # Exit a parse tree produced by EjemploParser#funcion.
    def exitFuncion(self, ctx:EjemploParser.FuncionContext):
        pass


    # Enter a parse tree produced by EjemploParser#argumentos.
    def enterArgumentos(self, ctx:EjemploParser.ArgumentosContext):
        pass

    # Exit a parse tree produced by EjemploParser#argumentos.
    def exitArgumentos(self, ctx:EjemploParser.ArgumentosContext):
        pass



del EjemploParser