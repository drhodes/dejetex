// -*- antlr -*-

lexer grammar DejeTexLexer;

channels {
  WHITESPACE_CHANNEL,
  COMMENTS_CHANNEL
}

AND : 'and' ;
OR : 'or' ;
NOT : 'not' ;

COMMA : ',' ;
DOT : '.' ;
SEMI : ';' ;

LPAREN : '(' ;
RPAREN : ')' ;
LCURLY : '{' ;
RCURLY : '}' ;

BEGIN : '\\begin' ;
END : '\\end' ;
NEWCOMMAND : '\\newcommand' ;

ADD : '+' ;
EQ : '=' ;
MUL : '*' ;
NEG : '-' ;
POW : '^' ;

DIV : '/' ;
NEWLINE : '\\n' ;
UNDERSCORE : '_' ;

CMD : [\\][a-zA-Z]+ ;
ID: [a-zA-Z][a-zA-Z0-9']+ ;
INT : [0-9]+ ;
WORD : [a-zA-Z0-9\\.]+ ;
WS: [ \t\n\r\f]+ -> channel(WHITESPACE_CHANNEL) ;

PERCENT : '%' ;

SingleLineComment : PERCENT ~[\n]* -> channel(HIDDEN);

UNSAFE : '\\begin{unsafe}' .*? '\\end{unsafe}' -> channel(HIDDEN) ;

