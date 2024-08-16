%{
#include <stdio.h>

#define IF 1
#define THEN 2
#define ELSE 3
#define ID 4
#define RELOP 5

void muestra(char* texto, int n);


%}


/* Expresiones regulares */
delim    [ \t\n]
ws       {delim}+
letter   [A-Za-z]
digit    [0-9]
id       {letter}({letter}|{digit})*


%%
{ws}        {/* No hacer nada. */}
if          muestra(yytext, IF);
then        muestra(yytext, THEN);
{id}        muestra(yytext, ID);
%%

void muestra(char* texto, int n) {
   printf("Es un %s que tiene código %d\n", texto, n);
}
