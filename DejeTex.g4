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
    | env
    | expr
    | mathmode
    ;

expr
    : num
    | punc
    | WORD
    | STRING   
    | ID
    | NEWLINE
    | input_cmd
    | param
    | LCURLY expr RCURLY
    | expr binop expr   
    | cmd
    ;

mathmode : DOLLAR expr* DOLLAR;

punc
    : COMMA
    | DOT
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


define
    : DEF CMD param? LCURLY stmt* RCURLY
    ;

input_cmd : INPUT LCURLY expr RCURLY ;
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
