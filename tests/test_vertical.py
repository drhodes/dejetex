from antlr4 import FileStream, CommonTokenStream
from dejetex.DejeTexLexer import DejeTexLexer
from dejetex.DejeTex import DejeTex
from dejetex.DejeTexVisitor import DejeTexVisitor


def vertical_test(name):
    input_filename = f"./tests/deje-tests/{name}.deje"  # Replace with your test filename
    input_stream = FileStream(input_filename)
    lexer = DejeTexLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = DejeTex(stream)
    tree = parser.program()
    if parser.getNumberOfSyntaxErrors() > 0:
        print(parser)
        raise Exception("syntax errors")
    else:
        vinterp = DejeTexVisitor()
        vinterp.visit(tree)



# def test_vertical(): vertical_test("vertical1")
