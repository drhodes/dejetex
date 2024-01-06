import sys
from antlr4 import *
from dejetex.DejeTexLexer import DejeTexLexer
from dejetex.DejeTex import DejeTex
from dejetex.DejeTexVisitor import DejeTexVisitor
from dejetex.check_env import check

def main():
    input_stream = FileStream(sys.argv[1])
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
    main()
