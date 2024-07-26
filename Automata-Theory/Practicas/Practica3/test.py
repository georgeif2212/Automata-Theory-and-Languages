import sys
from antlr4 import *
from EjemploLexer import EjemploLexer
from EjemploParser import EjemploParser


def main(argv):
    input = FileStream(argv[1])
    lexer = EjemploLexer(input)
    stream = CommonTokenStream(lexer)
    parser = EjemploParser(stream)
    tree = parser.programa()
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main(sys.argv)
