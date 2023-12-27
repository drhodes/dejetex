from antlr4 import FileStream, CommonTokenStream
from dejetex.DejeTexLexer import DejeTexLexer
from dejetex.DejeTex import DejeTex
from dejetex.DejeTexVisitor import DejeTexVisitor


def int_test(name):
    input_filename = f"./tests/deje-tests/{name}.deje"
    input_stream = FileStream(input_filename)
    lexer = DejeTexLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = DejeTex(stream)
    tree = parser.expr()
    if parser.getNumberOfSyntaxErrors() > 0:
        raise Exception("syntax errors")
    else:
        vinterp = DejeTexVisitor()
        vinterp.visit(tree)



def test_int1(): int_test("int1")
def test_int2(): int_test("int2")
