// -*- antlr -*-

lexer grammar DejeTexLexer;

channels {
  WHITESPACE_CHANNEL,
  COMMENTS_CHANNEL
}

COMMA : ',' ;
DOT   : '.' ;
SEMI  : ';' ;

LPAREN  : '(' ;
RPAREN  : ')' ;
LCURLY  : '{' ;
RCURLY  : '}' ;
LSQUARE : '[' ;
RSQUARE : ']' ;

BEGIN : '\\begin' ;
END   : '\\end'   ;
NEWCOMMAND : '\\newcommand' ;
USEPACKAGE : '\\usepackage' ;
INPUT : '\\input' ;
DEF : '\\def' ;


ADD : '+' ;
EQ  : '=' ;
MUL : '*' ;
NEG : '-' ;
POW : '^' ;
DIV : '/' ;
NEWLINE : '\\n' ;
UNDERSCORE : '_' ;
DQUOTE : '"';


CMD   : [\\][a-zA-Z]+ ;
ID    : [a-zA-Z][a-zA-Z0-9']+ ;
DIGIT : [0-9] ;
INT   : [0-9]+ ;
STRING : '"' (~[\r\n"])* '"' ;
WORD  : [a-zA-Z0-9.:]+ ;
WS    : [ \t\n\r\f]+ -> channel(WHITESPACE_CHANNEL) ;

PERCENT : '%' ;
HASH : '#' ;
BANG : '!';
DOLLAR : '$';

SingleLineComment
    : (PERCENT ~[\n]* | PERCENT [\n]) -> channel(HIDDEN);

UNSAFE : '\\begin' WS? '{' WS? 'unsafe' WS? '}' .*? '\\end' WS? '{' WS? 'unsafe' WS? '}' -> channel(HIDDEN) ;

