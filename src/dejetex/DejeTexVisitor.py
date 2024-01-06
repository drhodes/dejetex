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


    # Visit a parse tree produced by DejeTex#expr.
    def visitExpr(self, ctx:DejeTex.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DejeTex#punc.
    def visitPunc(self, ctx:DejeTex.PuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DejeTex#num.
    def visitNum(self, ctx:DejeTex.NumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DejeTex#env.
    def visitEnv(self, ctx:DejeTex.EnvContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DejeTex#args.
    def visitArgs(self, ctx:DejeTex.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DejeTex#cmd.
    def visitCmd(self, ctx:DejeTex.CmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DejeTex#define.
    def visitDefine(self, ctx:DejeTex.DefineContext):
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


    # Visit a parse tree produced by DejeTex#param.
    def visitParam(self, ctx:DejeTex.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DejeTex#new_command_simple.
    def visitNew_command_simple(self, ctx:DejeTex.New_command_simpleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DejeTex#new_command_optional_arguments.
    def visitNew_command_optional_arguments(self, ctx:DejeTex.New_command_optional_argumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DejeTex#newcommand.
    def visitNewcommand(self, ctx:DejeTex.NewcommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DejeTex#usepackage.
    def visitUsepackage(self, ctx:DejeTex.UsepackageContext):
        return self.visitChildren(ctx)



del DejeTex