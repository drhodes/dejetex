// -*- antlr -*-

parser grammar DejeTex;

options {
    tokenVocab = DejeTexLexer;
}

program
    : stmt* EOF
    ;

stmt: expr 
    | env
    ;

expr: INT
    | WORD
    | ID
    | NEWLINE
    | LCURLY expr RCURLY
    | expr binop expr
    | cmd
    ;

env : begin (stmt)* end ;

cmd : CMD (LCURLY stmt* RCURLY)* ;

begin : BEGIN LCURLY ID RCURLY ;
end : END LCURLY ID RCURLY ;
binop: POW | ADD | NEG | MUL | DIV | UNDERSCORE | EQ ;

// \newcommand{\<env-name>}[<n-args>][<default>]{<begin-code>}
// \newcommand{\end<env-name>}{<end-code>}

// newcommand : NEWCOMMAND '{' '\\' ID '}' '[' INT ']' ('[' cmd ']')? '{' stmt+ '}' ;


