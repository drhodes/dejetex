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

def sum_test(name):
    def inner(parser):
        tree = parser.cmd()
        if parser.getNumberOfSyntaxErrors() > 0:
            raise Exception("syntax errors")
        else:
            vinterp = DejeTexVisitor()
            vinterp.visit(tree)
        
    generic_test(inner, name)


def test_sum_int1(): sum_test("sum1")
