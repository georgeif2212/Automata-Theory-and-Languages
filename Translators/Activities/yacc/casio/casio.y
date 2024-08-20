%token ENTERO VARIABLE
%left '+' '-'
%left '*' '/'

%{
#include <stdio.h>
#include "lex.yy.c"

int sym[26]; /* tabla de símbolos */
%}

%%

programa:
   programa oracion '\n'
   |
   ;

oracion:
   expr                    { printf("%d\n", $1); }
   | VARIABLE '=' expr     { sym[$1] = $3; }
   ;

expr:
   ENTERO
   | VARIABLE              { $$ = sym[$1]; }
   | expr '+' expr         { $$ = $1 + $3; }
   | expr '-' expr         { $$ = $1 - $3; }
   | expr '*' expr         { $$ = $1 * $3; }
   | expr '/' expr         { $$ = $1 / $3; }
   | '(' expr ')'          { $$ = $2; }
   ;

%%


int main(void) {
   yyparse();
   return 0;
}

