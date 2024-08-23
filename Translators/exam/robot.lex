%{
#include <stdlib.h>
//#include "casio_plus.h"
#include "y.tab.h"

int yyerror(const char *s);
int yylex();
extern "C" int yywrap();

%}


%%


[a-z]          {
                    yylval.sIndex = *yytext - 'a';
                    return VARIABLE;
                }

[0-9]+         {
                    yylval.iValue = atoi(yytext);
                    return INTEGER;
                }

[-()<>=+*/,;{}.] { return *yytext; }

    /*">="        return GE;*/
    /*"<="        return LE;*/
    /*"=="        return EQ;*/
    /*"!="        return NE;*/
    /*"&&"        return AND;*/
    /*"||"        return OR;*/
    
    /*"else"      return ELSE;*/
    /*"print"     return PRINT; */

"Avanzar"           return MOVE;
"GirarIzquierda"    return TURNLEFT;
"hayPared"          return ISWALL;
"no"                return NO;
"Mientras"          return WHILE;
"if"                return IF;
"Hacer"             return DO;
"Inicio"            return START;
"Fin"               return END;
"Apagar"            return TURNOFF;





[ \t\n+]    ;       /* ignore whitespace */

.           yyerror("token no reconocido.");

%%

int yyerror(const char *s) {
    fprintf(stderr, "%s\n", s);
    return 0;
}


extern "C" int yywrap( void ) {
    return 1;
}