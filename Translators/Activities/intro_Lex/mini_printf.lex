%{
#include <stdio.h>

#define IF 1
#define THEN 2
#define ELSE 3
#define ID 4
#define RELOP 5
%}


/* Expresiones regulares */
delim    [ \t\n]
ws       {delim}+
letter   [A-Za-z]
digit    [0-9]
id       {letter}({letter}|{digit})*


%%
{ws}        {/* No hacer nada. */}
if          printf("Es un if con código %d\n", IF);
then        printf("Es un then con código %d\n", THEN);
else        printf("Es un else con código %d\n", ELSE);
{id}        printf("Es un identificador con código %d\n", ID);
"<"         printf("Es un menor con código %d\n", RELOP);

%%

