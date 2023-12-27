# Generated from DejeTex.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .DejeTex import DejeTex
else:
    from DejeTex import DejeTex

# This class defines a complete generic visitor for a parse tree produced by DejeTex.

class DejeTexVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DejeTex#program.
    def visitProgram(self, ctx:DejeTex.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DejeTex#stmt.
    def visitStmt(self, ctx:DejeTex.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DejeTex#env.
    def visitEnv(self, ctx:DejeTex.EnvContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DejeTex#expr.
    def visitExpr(self, ctx:DejeTex.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DejeTex#cmd.
    def visitCmd(self, ctx:DejeTex.CmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DejeTex#begin.
    def visitBegin(self, ctx:DejeTex.BeginContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DejeTex#end.
    def visitEnd(self, ctx:DejeTex.EndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DejeTex#binop.
    def visitBinop(self, ctx:DejeTex.BinopContext):
        return self.visitChildren(ctx)



del DejeTex