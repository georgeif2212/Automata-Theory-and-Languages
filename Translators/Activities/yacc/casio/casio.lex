%{
#include "y.tab.h"   // Este archivo lo generará Yacc.

int yyerror( char *s );
int yylex();
int yywrap();

%}

%%
   /* Variables: su valor será 0 para ‘a’, 1 para ‘b’,... */
[a-z]          {
                  yylval = *yytext - 'a';
                  return VARIABLE;
               }

   /* Variables: su valor será 0 para ‘a’, 1 para ‘b’,... */
[0-9]+         {
                  yylval = atoi(yytext);
                  return ENTERO;
               }

   /* Variables: su valor será 0 para ‘a’, 1 para ‘b’,... */
[-+()=/*\n]    { return *yytext; }

   /* Ignorar espacios en blanco y tabulares */
[ \t]          ;

   /* Si no coincide con ninguna ER de arriba... */
.              yyerror("token no reconocido.");


%%

int yyerror( char *s ) { fprintf( stderr, "%s\n", s); }

int yywrap(void) {
   return 1;
}
