import sys
from antlr4 import *
from DejeTexLexer import DejeTexLexer
from DejeTexParser import DejeTexParser
from DejeTexVisitor import DejeTexVisitor

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = DejeTexLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = DejeTexParser(stream)
    tree = parser.expr()
    if parser.getNumberOfSyntaxErrors() > 0:
        print("syntax errors")
    else:
        vinterp = DejeTexVisitor()
        vinterp.visit(tree)

if __name__ == '__main__':
    main(sys.argv)
