# Generated from ./Skyline.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("J\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\3\2\5\2\r\n\2\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3\27\n\3\f\3\16\3\32")
        buf.write("\13\3\5\3\34\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3/\n\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3=\n\3\f\3\16\3@")
        buf.write("\13\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\2\3\4\5\2\4")
        buf.write("\6\2\3\3\2\5\6\2R\2\f\3\2\2\2\4.\3\2\2\2\6A\3\2\2\2\b")
        buf.write("\t\7\17\2\2\t\n\7\3\2\2\n\r\5\4\3\2\13\r\5\4\3\2\f\b\3")
        buf.write("\2\2\2\f\13\3\2\2\2\r\3\3\2\2\2\16\17\b\3\1\2\17\20\7")
        buf.write("\6\2\2\20/\5\4\3\f\21/\5\6\4\2\22\33\7\n\2\2\23\30\5\6")
        buf.write("\4\2\24\25\7\4\2\2\25\27\5\6\4\2\26\24\3\2\2\2\27\32\3")
        buf.write("\2\2\2\30\26\3\2\2\2\30\31\3\2\2\2\31\34\3\2\2\2\32\30")
        buf.write("\3\2\2\2\33\23\3\2\2\2\33\34\3\2\2\2\34\35\3\2\2\2\35")
        buf.write("/\7\13\2\2\36\37\7\f\2\2\37 \7\16\2\2 !\7\4\2\2!\"\7\16")
        buf.write("\2\2\"#\7\4\2\2#$\7\16\2\2$%\7\4\2\2%&\7\16\2\2&\'\7\4")
        buf.write("\2\2\'(\7\16\2\2(/\7\r\2\2)*\7\b\2\2*+\5\4\3\2+,\7\t\2")
        buf.write("\2,/\3\2\2\2-/\7\17\2\2.\16\3\2\2\2.\21\3\2\2\2.\22\3")
        buf.write("\2\2\2.\36\3\2\2\2.)\3\2\2\2.-\3\2\2\2/>\3\2\2\2\60\61")
        buf.write("\f\13\2\2\61\62\7\7\2\2\62=\5\4\3\f\63\64\f\t\2\2\64\65")
        buf.write("\7\5\2\2\65=\5\4\3\n\66\67\f\n\2\2\678\7\7\2\28=\7\16")
        buf.write("\2\29:\f\b\2\2:;\t\2\2\2;=\7\16\2\2<\60\3\2\2\2<\63\3")
        buf.write("\2\2\2<\66\3\2\2\2<9\3\2\2\2=@\3\2\2\2><\3\2\2\2>?\3\2")
        buf.write("\2\2?\5\3\2\2\2@>\3\2\2\2AB\7\b\2\2BC\7\16\2\2CD\7\4\2")
        buf.write("\2DE\7\16\2\2EF\7\4\2\2FG\7\16\2\2GH\7\t\2\2H\7\3\2\2")
        buf.write("\2\b\f\30\33.<>")
        return buf.getvalue()


class SkylineParser ( Parser ):

    grammarFileName = "Skyline.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':='", "','", "'+'", "'-'", "'*'", "'('", 
                     "')'", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "ASSIGN", "COMMA", "PLUS", "MINUS", "ASTERISK", 
                      "LPAR", "RPAR", "LBRA", "RBRA", "LCUR", "RCUR", "INTEGER", 
                      "ID", "WS" ]

    RULE_command = 0
    RULE_skyline = 1
    RULE_building = 2

    ruleNames =  [ "command", "skyline", "building" ]

    EOF = Token.EOF
    ASSIGN=1
    COMMA=2
    PLUS=3
    MINUS=4
    ASTERISK=5
    LPAR=6
    RPAR=7
    LBRA=8
    RBRA=9
    LCUR=10
    RCUR=11
    INTEGER=12
    ID=13
    WS=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CommandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SkylineParser.RULE_command

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class EvaluateContext(CommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.CommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def skyline(self):
            return self.getTypedRuleContext(SkylineParser.SkylineContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEvaluate" ):
                return visitor.visitEvaluate(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(CommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.CommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SkylineParser.ID, 0)
        def ASSIGN(self):
            return self.getToken(SkylineParser.ASSIGN, 0)
        def skyline(self):
            return self.getTypedRuleContext(SkylineParser.SkylineContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)



    def command(self):

        localctx = SkylineParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_command)
        try:
            self.state = 10
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                localctx = SkylineParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 6
                self.match(SkylineParser.ID)
                self.state = 7
                self.match(SkylineParser.ASSIGN)
                self.state = 8
                self.skyline(0)
                pass

            elif la_ == 2:
                localctx = SkylineParser.EvaluateContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 9
                self.skyline(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SkylineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SkylineParser.RULE_skyline

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ReplicationContext(SkylineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.SkylineContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def skyline(self):
            return self.getTypedRuleContext(SkylineParser.SkylineContext,0)

        def ASTERISK(self):
            return self.getToken(SkylineParser.ASTERISK, 0)
        def INTEGER(self):
            return self.getToken(SkylineParser.INTEGER, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReplication" ):
                return visitor.visitReplication(self)
            else:
                return visitor.visitChildren(self)


    class SinglebuildingContext(SkylineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.SkylineContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def building(self):
            return self.getTypedRuleContext(SkylineParser.BuildingContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSinglebuilding" ):
                return visitor.visitSinglebuilding(self)
            else:
                return visitor.visitChildren(self)


    class MirrorContext(SkylineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.SkylineContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(SkylineParser.MINUS, 0)
        def skyline(self):
            return self.getTypedRuleContext(SkylineParser.SkylineContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMirror" ):
                return visitor.visitMirror(self)
            else:
                return visitor.visitChildren(self)


    class IdentContext(SkylineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.SkylineContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SkylineParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdent" ):
                return visitor.visitIdent(self)
            else:
                return visitor.visitChildren(self)


    class IntersectionContext(SkylineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.SkylineContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def skyline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.SkylineContext)
            else:
                return self.getTypedRuleContext(SkylineParser.SkylineContext,i)

        def ASTERISK(self):
            return self.getToken(SkylineParser.ASTERISK, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntersection" ):
                return visitor.visitIntersection(self)
            else:
                return visitor.visitChildren(self)


    class TranslationContext(SkylineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.SkylineContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def skyline(self):
            return self.getTypedRuleContext(SkylineParser.SkylineContext,0)

        def INTEGER(self):
            return self.getToken(SkylineParser.INTEGER, 0)
        def PLUS(self):
            return self.getToken(SkylineParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(SkylineParser.MINUS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTranslation" ):
                return visitor.visitTranslation(self)
            else:
                return visitor.visitChildren(self)


    class UnionContext(SkylineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.SkylineContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def skyline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.SkylineContext)
            else:
                return self.getTypedRuleContext(SkylineParser.SkylineContext,i)

        def PLUS(self):
            return self.getToken(SkylineParser.PLUS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnion" ):
                return visitor.visitUnion(self)
            else:
                return visitor.visitChildren(self)


    class ParenthesisContext(SkylineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.SkylineContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAR(self):
            return self.getToken(SkylineParser.LPAR, 0)
        def skyline(self):
            return self.getTypedRuleContext(SkylineParser.SkylineContext,0)

        def RPAR(self):
            return self.getToken(SkylineParser.RPAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthesis" ):
                return visitor.visitParenthesis(self)
            else:
                return visitor.visitChildren(self)


    class MultiplebuildingsContext(SkylineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.SkylineContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LBRA(self):
            return self.getToken(SkylineParser.LBRA, 0)
        def RBRA(self):
            return self.getToken(SkylineParser.RBRA, 0)
        def building(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.BuildingContext)
            else:
                return self.getTypedRuleContext(SkylineParser.BuildingContext,i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.COMMA)
            else:
                return self.getToken(SkylineParser.COMMA, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplebuildings" ):
                return visitor.visitMultiplebuildings(self)
            else:
                return visitor.visitChildren(self)


    class RandommultiplebuildingsContext(SkylineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.SkylineContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LCUR(self):
            return self.getToken(SkylineParser.LCUR, 0)
        def INTEGER(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.INTEGER)
            else:
                return self.getToken(SkylineParser.INTEGER, i)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.COMMA)
            else:
                return self.getToken(SkylineParser.COMMA, i)
        def RCUR(self):
            return self.getToken(SkylineParser.RCUR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRandommultiplebuildings" ):
                return visitor.visitRandommultiplebuildings(self)
            else:
                return visitor.visitChildren(self)



    def skyline(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SkylineParser.SkylineContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_skyline, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = SkylineParser.MirrorContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 13
                self.match(SkylineParser.MINUS)
                self.state = 14
                self.skyline(10)
                pass

            elif la_ == 2:
                localctx = SkylineParser.SinglebuildingContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 15
                self.building()
                pass

            elif la_ == 3:
                localctx = SkylineParser.MultiplebuildingsContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 16
                self.match(SkylineParser.LBRA)
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SkylineParser.LPAR:
                    self.state = 17
                    self.building()
                    self.state = 22
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==SkylineParser.COMMA:
                        self.state = 18
                        self.match(SkylineParser.COMMA)
                        self.state = 19
                        self.building()
                        self.state = 24
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 27
                self.match(SkylineParser.RBRA)
                pass

            elif la_ == 4:
                localctx = SkylineParser.RandommultiplebuildingsContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 28
                self.match(SkylineParser.LCUR)
                self.state = 29
                self.match(SkylineParser.INTEGER)
                self.state = 30
                self.match(SkylineParser.COMMA)
                self.state = 31
                self.match(SkylineParser.INTEGER)
                self.state = 32
                self.match(SkylineParser.COMMA)
                self.state = 33
                self.match(SkylineParser.INTEGER)
                self.state = 34
                self.match(SkylineParser.COMMA)
                self.state = 35
                self.match(SkylineParser.INTEGER)
                self.state = 36
                self.match(SkylineParser.COMMA)
                self.state = 37
                self.match(SkylineParser.INTEGER)
                self.state = 38
                self.match(SkylineParser.RCUR)
                pass

            elif la_ == 5:
                localctx = SkylineParser.ParenthesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 39
                self.match(SkylineParser.LPAR)
                self.state = 40
                self.skyline(0)
                self.state = 41
                self.match(SkylineParser.RPAR)
                pass

            elif la_ == 6:
                localctx = SkylineParser.IdentContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 43
                self.match(SkylineParser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 60
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 58
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = SkylineParser.IntersectionContext(self, SkylineParser.SkylineContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_skyline)
                        self.state = 46
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 47
                        self.match(SkylineParser.ASTERISK)
                        self.state = 48
                        self.skyline(10)
                        pass

                    elif la_ == 2:
                        localctx = SkylineParser.UnionContext(self, SkylineParser.SkylineContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_skyline)
                        self.state = 49
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 50
                        self.match(SkylineParser.PLUS)
                        self.state = 51
                        self.skyline(8)
                        pass

                    elif la_ == 3:
                        localctx = SkylineParser.ReplicationContext(self, SkylineParser.SkylineContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_skyline)
                        self.state = 52
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 53
                        self.match(SkylineParser.ASTERISK)
                        self.state = 54
                        self.match(SkylineParser.INTEGER)
                        pass

                    elif la_ == 4:
                        localctx = SkylineParser.TranslationContext(self, SkylineParser.SkylineContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_skyline)
                        self.state = 55
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 56
                        _la = self._input.LA(1)
                        if not(_la==SkylineParser.PLUS or _la==SkylineParser.MINUS):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 57
                        self.match(SkylineParser.INTEGER)
                        pass

             
                self.state = 62
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class BuildingContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SkylineParser.RULE_building

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class OnebuildingContext(BuildingContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.BuildingContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAR(self):
            return self.getToken(SkylineParser.LPAR, 0)
        def INTEGER(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.INTEGER)
            else:
                return self.getToken(SkylineParser.INTEGER, i)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.COMMA)
            else:
                return self.getToken(SkylineParser.COMMA, i)
        def RPAR(self):
            return self.getToken(SkylineParser.RPAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOnebuilding" ):
                return visitor.visitOnebuilding(self)
            else:
                return visitor.visitChildren(self)



    def building(self):

        localctx = SkylineParser.BuildingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_building)
        try:
            localctx = SkylineParser.OnebuildingContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(SkylineParser.LPAR)
            self.state = 64
            self.match(SkylineParser.INTEGER)
            self.state = 65
            self.match(SkylineParser.COMMA)
            self.state = 66
            self.match(SkylineParser.INTEGER)
            self.state = 67
            self.match(SkylineParser.COMMA)
            self.state = 68
            self.match(SkylineParser.INTEGER)
            self.state = 69
            self.match(SkylineParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.skyline_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def skyline_sempred(self, localctx:SkylineContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         




