# Generated from ./Skyline.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
else:
    from SkylineParser import SkylineParser

# This class defines a complete generic visitor for a parse tree produced by SkylineParser.

class SkylineVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SkylineParser#assign.
    def visitAssign(self, ctx:SkylineParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#evaluate.
    def visitEvaluate(self, ctx:SkylineParser.EvaluateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#replication.
    def visitReplication(self, ctx:SkylineParser.ReplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#singlebuilding.
    def visitSinglebuilding(self, ctx:SkylineParser.SinglebuildingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#mirror.
    def visitMirror(self, ctx:SkylineParser.MirrorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#ident.
    def visitIdent(self, ctx:SkylineParser.IdentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#intersection.
    def visitIntersection(self, ctx:SkylineParser.IntersectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#translation.
    def visitTranslation(self, ctx:SkylineParser.TranslationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#union.
    def visitUnion(self, ctx:SkylineParser.UnionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#parenthesis.
    def visitParenthesis(self, ctx:SkylineParser.ParenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#multiplebuildings.
    def visitMultiplebuildings(self, ctx:SkylineParser.MultiplebuildingsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#randommultiplebuildings.
    def visitRandommultiplebuildings(self, ctx:SkylineParser.RandommultiplebuildingsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#onebuilding.
    def visitOnebuilding(self, ctx:SkylineParser.OnebuildingContext):
        return self.visitChildren(ctx)



del SkylineParser