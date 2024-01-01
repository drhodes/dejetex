// -*- antlr -*-

parser grammar DejeTex;

options {
    tokenVocab = DejeTexLexer;
}

program
    : stmt* EOF
    ;

stmt
    : newcommand
    | usepackage
    | define        
    | expr
    | env
    ;

expr
    : num
    | punc
    | WORD
    | STRING
    | ID
    | NEWLINE
    | param
    | LCURLY expr RCURLY
    | expr binop expr   
    | cmd
    ;

punc
    : COMMA 
    | BANG
    | LPAREN
    | RPAREN
    ;

num : INT
    | DIGIT
    ;

env : begin (stmt)* end ;

args
    : (LCURLY stmt* RCURLY)+
    | (LSQUARE stmt* RSQUARE)+
    ;

cmd : CMD args* ;

// \def <command> <parameter-text>{<replacement-text>}
// \def\start{start="2023-09-06T15:00"}
// def is a python keyword, so use "define" as grammar rule
define : DEF CMD LCURLY stmt* RCURLY ;


begin : BEGIN LCURLY ID RCURLY args*;
end : END LCURLY ID RCURLY ;
binop: POW | ADD | NEG | MUL | DIV | UNDERSCORE | EQ ;

param : HASH DIGIT;

new_command_simple :
        NEWCOMMAND
        LCURLY CMD RCURLY
        LCURLY stmt+ RCURLY;

new_command_optional_arguments :
        NEWCOMMAND
        LCURLY CMD RCURLY
        LSQUARE DIGIT RSQUARE
        LCURLY stmt+ RCURLY;

// \newcommand{\<env-name>}[<n-args>][<default>]{<begin-code>}
// \newcommand{\end<env-name>}{<end-code>}

newcommand
    : new_command_simple
    | new_command_optional_arguments
    ;

// \usepackage{cancel}
usepackage
    : USEPACKAGE LCURLY (ID COMMA)* ID RCURLY ;



// Simple commands
// Commands with parameters
// Commands with optional parameters
