# Generated from DejeTex.g4 by ANTLR 4.13.1

from DejeTex import DejeTex
from DejeTexVisitor import DejeTexVisitor

class CheckEnvVisitor(DejeTexVisitor):
    # Visit a parse tree produced by DejeTex#env.
    def visitEnv(self, ctx:DejeTex.EnvContext):
        env_begin_id = ctx.begin().getChild(2).getText()
        env_end_id = ctx.end().getChild(2).getText()

        # print(f"checking: {env_begin_id} == {env_end_id}")
        assert(env_begin_id == env_end_id)
        return self.visitChildren(ctx)

    
def check(text, tree):
    
    checker = CheckEnvVisitor()
    checker_result = checker.visit(tree)

    print(f"Original Expression: {text}")
    print(f"Checked: {checker_result}")

