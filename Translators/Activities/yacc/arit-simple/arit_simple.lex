%{
#include "y.tab.h"
#include <stdio.h>
%}


%%

[0-9]+  {yylval =atoi(yytext);return ENTERO;}

[-+*/\n]    {return *yytext;}

[\t]    ;

.   fprintf(stderr,"token no reconocido: %s", yytext);

%%

int yywrap(void){
    return 1;
}

// HOW TO COMPILE USING YACC 
/*
    1. Compile lex file to generate DFA
        lex name_file.lex -> lex.yy.c

    2. Compile YACC
        $ yacc -H name_file.y   -> y.tab.c
                                -> y.tab.h

    3. Compile
        gcc -lfl y.tab.c -o name_exe  
*/