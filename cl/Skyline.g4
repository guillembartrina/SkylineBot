
grammar Skyline;


//Rules

command : ID ASSIGN skyline     #assign //assingation
        | skyline               #evaluate //skyline
        ;

skyline : MINUS skyline                                                                 #mirror //skyline mirror
        | skyline ASTERISK skyline                                                      #intersection //skylines intersection
        | skyline ASTERISK INTEGER                                                      #replication //skyline replication
        | skyline PLUS skyline                                                          #union //skylines union
        | skyline (PLUS|MINUS) INTEGER                                                  #translation //skyline translation
        | building                                                                      #singlebuilding //single building
        | LBRA (building (COMMA building)*)? RBRA                                       #multiplebuildings //multiple buildings
        | LCUR INTEGER COMMA INTEGER COMMA INTEGER COMMA INTEGER COMMA INTEGER RCUR     #randommultiplebuildings //random multiple buildings
        | LPAR skyline RPAR                                                             #parenthesis //parenthesis          
        | ID                                                                            #ident //stored skyline
        ;

building : LPAR INTEGER COMMA INTEGER COMMA INTEGER RPAR        #onebuilding//single building definition
         ;


//Tokens

ASSIGN : ':=' ;

COMMA : ',' ;

PLUS : '+' ;
MINUS : '-' ;
ASTERISK : '*' ;

LPAR : '(' ;
RPAR : ')' ;
LBRA : '[' ;
RBRA : ']' ;
LCUR : '{' ;
RCUR : '}' ;

INTEGER : [0-9]+ ;

ID : [a-zA-Z] [a-zA-Z0-9]* ;

//skip: ws, tab, nl
WS : [ \t\n]+ -> skip ; 