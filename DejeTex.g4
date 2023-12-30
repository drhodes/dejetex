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
    | expr
    | env
    ;

expr
    : num
    | WORD
    | ID
    | NEWLINE
    | param
    | LCURLY expr RCURLY
    | expr binop expr   
    | cmd
    ;

num : INT
    | DIGIT
    ;

env : begin (stmt)* end ;

cmd : CMD (LCURLY stmt* RCURLY)* ;

begin : BEGIN LCURLY ID RCURLY ;
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

newcommand
    : new_command_simple
    | new_command_optional_arguments
    ; 


// \newcommand{\<env-name>}[<n-args>][<default>]{<begin-code>}
// \newcommand{\end<env-name>}{<end-code>}



// Simple commands
// Commands with parameters
// Commands with optional parameters
