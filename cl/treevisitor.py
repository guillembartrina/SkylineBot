import sys
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from cl.SkylineLexer import SkylineLexer
from cl.SkylineParser import SkylineParser
from cl.SkylineVisitor import SkylineVisitor
from skyline import generateRandomBuildings, skylineFromBuildings, Skyline


class CustomErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception("[Error de parsing]")


def parse(text):
    inputStream = InputStream(text)
    lexer = SkylineLexer(inputStream)
    lexer.addErrorListener(CustomErrorListener())
    tokenStream = CommonTokenStream(lexer)
    parser = SkylineParser(tokenStream)
    parser.addErrorListener(CustomErrorListener())
    tree = parser.command()
    try:
        visitor = Visitor()
        return visitor.visit(tree)
    except Warning as err:
        raise Exception("[" + str(err) + "]")
    except Exception as err:
        raise Exception("[Error de visitor: " + str(err) + "]")


class Visitor(SkylineVisitor):

    skylines = {}

    def visitAssign(self, ctx: SkylineParser.AssignContext):
        skyline = self.visit(ctx.skyline())
        Visitor.skylines[ctx.ID().getText()] = skyline
        return skyline

    def visitEvaluate(self, ctx: SkylineParser.EvaluateContext):
        skyline = self.visit(ctx.skyline())
        return skyline

    def visitReplication(self, ctx: SkylineParser.ReplicationContext):
        skyline = self.visit(ctx.skyline())
        number = int(ctx.INTEGER().getText())
        return skyline * number

    def visitSinglebuilding(self, ctx: SkylineParser.SinglebuildingContext):
        building = self.visit(ctx.building())
        skyline = Skyline([building])
        return skyline

    def visitMirror(self, ctx: SkylineParser.MirrorContext):
        skyline = self.visit(ctx.skyline())
        return -skyline

    def visitIdent(self, ctx: SkylineParser.IdentContext):
        try:
            skyline = Visitor.skylines[ctx.ID().getText()]
            return skyline
        except KeyError:
            raise Warning("skyline '" + ctx.ID().getText() + "' no definit")

    def visitIntersection(self, ctx: SkylineParser.IntersectionContext):
        skyline0 = self.visit(ctx.skyline(0))
        skyline1 = self.visit(ctx.skyline(1))
        return skyline0 * skyline1

    def visitTranslation(self, ctx: SkylineParser.TranslationContext):
        skyline = self.visit(ctx.skyline())
        number = int(ctx.INTEGER().getText())
        operator = [child for child in ctx.getChildren()][1]
        if operator.getSymbol().type == SkylineParser.PLUS:
            return skyline + number
        elif operator.getSymbol().type == SkylineParser.MINUS:
            return skyline - number

    def visitUnion(self, ctx: SkylineParser.UnionContext):
        skyline0 = self.visit(ctx.skyline(0))
        skyline1 = self.visit(ctx.skyline(1))
        return skyline0 + skyline1

    def visitParenthesis(self, ctx: SkylineParser.ParenthesisContext):
        skyline = self.visit(ctx.skyline())
        return skyline

    def visitMultiplebuildings(self, ctx: SkylineParser.MultiplebuildingsContext):
        buildings = []
        for b in ctx.building():
            building = self.visit(b)
            buildings.append(building)
        skyline = skylineFromBuildings(buildings)
        return skyline

    def visitRandommultiplebuildings(self, ctx: SkylineParser.RandommultiplebuildingsContext):
        nn = int(ctx.INTEGER(0).getText())
        hh = int(ctx.INTEGER(1).getText())
        ww = int(ctx.INTEGER(2).getText())
        xmin = int(ctx.INTEGER(3).getText())
        xmax = int(ctx.INTEGER(4).getText())
        if hh <= 0:
            raise Warning("altura incorrecte")
        elif ww <= 0:
            raise Warning("amplada incorrecte")
        elif xmin > xmax:
            raise Warning("min i max incorrectes")
        skyline = skylineFromBuildings(generateRandomBuildings(nn, hh, ww, xmin, xmax))
        return skyline

    def visitOnebuilding(self, ctx: SkylineParser.BuildingContext):
        ss = int(ctx.INTEGER(0).getText())
        hh = int(ctx.INTEGER(1).getText())
        ee = int(ctx.INTEGER(2).getText())
        if hh <= 0:
            raise Warning("altura incorrecte")
        elif ss >= ee:
            raise Warning("inici i final incorrectes")
        building = (ss, hh, ee)
        return building
