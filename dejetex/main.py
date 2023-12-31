import sys
from antlr4 import *
from DejeTexLexer import DejeTexLexer
from DejeTex import DejeTex
from DejeTexVisitor import DejeTexVisitor
from check_env import check

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = DejeTexLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = DejeTex(stream)
    tree = parser.program()
    if parser.getNumberOfSyntaxErrors() > 0:
        print("syntax errors")
    else:
        # vinterp = DejeTexVisitor()
        # vinterp.visit(tree)
        check(tree, tree)

        
if __name__ == '__main__':
    main(sys.argv)
