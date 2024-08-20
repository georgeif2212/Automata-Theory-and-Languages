%{
#include <stdio.h>
#include "arit_simple.yy.c"

int yyerror( char *s );
int yylex();
int yywrap();

%}

%token ENTERO
%left '+' '-'


%%

program:
   program expr '\n'    { printf("%d\n", $2); }
   |
   ;

expr:
   ENTERO			      { printf("\nEntero: %d", $1); }
   | expr '+' expr		{ printf("\nargs: %d y %d\n", $1, $3); }
	| expr '-' expr		{ printf("\nargs: %d y %d\n", $1, $3); }
   ;
%%

int main() {
   return yyparse();
}


int yyerror( char *s ) { fprintf( stderr, "%s\n", s); }