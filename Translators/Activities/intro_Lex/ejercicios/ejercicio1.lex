%{
#include <stdio.h>

#define PRIMER 1
#define SEGUNDO 2
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
01*|10*          printf("Es un 01* o 10* con código %d\n", PRIMER);
1*(01+)*|1*(01+)*0          printf("Es un 1*(01+)* o 1*(01+)*0 con código %d\n", SEGUNDO);
%%

// HOW TO EXECUTE?
/*
    1. Compile lex file to generate DFA
        lex name_file.lex -> lex.yy.c

    2. Compile the DFA code to get the recognizer executable
        gcc -lfl lex.yy.c -o name_file

    3. Execute
        ./name_file

*/