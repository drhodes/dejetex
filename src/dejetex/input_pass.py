# from dejetex.parse import parse
from antlr4 import *
from dejetex.DejeTex import DejeTex
from dejetex.DejeTexLexer import DejeTexLexer
from dejetex.DejeTexVisitor import DejeTexVisitor
import sys

class InputPass(DejeTexVisitor):
    # Visit a parse tree produced by DejeTex#env.
    def visitInput_cmd(self, ctx:DejeTex.Input_cmdContext):
        infile = ctx.getChild(2).getText()
        parse(infile)
        return self.visitChildren(ctx)

def parse(fname):
    input_stream = FileStream(fname)
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
        input_pass(tree, tree)
    
def input_pass(text, tree):
    ipass = InputPass()
    ipass.visit(tree)

