from dejetex.DejeTex import DejeTex
from dejetex.DejeTexVisitor import DejeTexVisitor

class CheckEnvVisitor(DejeTexVisitor):
    # Visit a parse tree produced by DejeTex#env.
    def visitEnv(self, ctx:DejeTex.EnvContext):
        env_begin_id = ctx.begin().getChild(2).getText()
        env_end_id = ctx.end().getChild(2).getText()

        # print(f"checking: {env_begin_id} == {env_end_id}")
        if not env_begin_id == env_end_id:
            print(f"invalid environment: starting on line {ctx.getSourceInterval()[0]}")
            print(f"  {ctx.begin().getText()}")
            print("")
            print(f"and ending on line {ctx.getSourceInterval()[1]}")
            print(f"  {ctx.end().getText()}")            
        return self.visitChildren(ctx)

    
def check(text, tree):
    
    checker = CheckEnvVisitor()
    checker_result = checker.visit(tree)

    # print(f"Original Expression: {text}")
    # print(f"Checked: {checker_result}")

