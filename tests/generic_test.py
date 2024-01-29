from antlr4 import FileStream, CommonTokenStream
from dejetex.DejeTexLexer import DejeTexLexer
from dejetex.DejeTex import DejeTex
from dejetex.DejeTexVisitor import DejeTexVisitor


def generic_test(inner, name):
    input_filename = f"./tests/deje-tests/{name}.deje"
    input_stream = FileStream(input_filename)
    lexer = DejeTexLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = DejeTex(stream)
    inner(parser)

def cmd_test(name):
    def inner(parser):
        tree = parser.cmd()
        if parser.getNumberOfSyntaxErrors() > 0:
            raise Exception("syntax errors")
        else:
            vinterp = DejeTexVisitor()
            vinterp.visit(tree)
    generic_test(inner, name)

def program_test(name):
    def inner(parser):
        tree = parser.program()
        if parser.getNumberOfSyntaxErrors() > 0:
            raise Exception("syntax errors")
        else:
            vinterp = DejeTexVisitor()
            vinterp.visit(tree)
    generic_test(inner, name)
    
def input_test(name):
    def inner(parser):
        tree = parser.input_cmd()
        if parser.getNumberOfSyntaxErrors() > 0:
            raise Exception("syntax errors")
        else:
            vinterp = DejeTexVisitor()
            vinterp.visit(tree)
    generic_test(inner, name)


def newcommand_test(name):
    def inner(parser):
        tree = parser.newcommand()
        if parser.getNumberOfSyntaxErrors() > 0:
            raise Exception("syntax errors")
        else:
            vinterp = DejeTexVisitor()
            vinterp.visit(tree)
    generic_test(inner, name)


def usepackage_test(name):
    def inner(parser):
        tree = parser.usepackage()
        if parser.getNumberOfSyntaxErrors() > 0:
            raise Exception("syntax errors")
        else:
            vinterp = DejeTexVisitor()
            vinterp.visit(tree)
    generic_test(inner, name)
    
def env_test(name):
    def inner(parser):
        tree = parser.env()
        if parser.getNumberOfSyntaxErrors() > 0:
            raise Exception("syntax errors")
        else:
            vinterp = DejeTexVisitor()
            vinterp.visit(tree)
    generic_test(inner, name)
    
def define_test(name):
    def inner(parser):
        tree = parser.define()
        if parser.getNumberOfSyntaxErrors() > 0:
            raise Exception("syntax errors")
        else:
            vinterp = DejeTexVisitor()
            vinterp.visit(tree)
    generic_test(inner, name)
    

def mathmode_inline_test(name):
    def inner(parser):
        tree = parser.mathmode_inline()
        if parser.getNumberOfSyntaxErrors() > 0:
            raise Exception("syntax errors")
        else:
            vinterp = DejeTexVisitor()
            vinterp.visit(tree)
    generic_test(inner, name)
    
    
