%{
#include <stdlib.h>
#include "y.tab.h"

extern "C" int yyerror(const char *s);
extern "C" int yylex();
extern "C" int yywrap();


%}


%%

[-()<>=+*/,;{}.] { return *yytext; }

">="        return GE;
"<="        return LE;
"=="        return EQ;
"!="        return NE;
"&&"        return AND;
"||"        return OR;

"while"     return WHILE;
"for"       return FOR;
"if"        return IF;
"else"      return ELSE;
"print"     return PRINT;
"to"        return TO; 

[a-zA-Z][a-zA-Z0-9_]*    { 
                            strcpy(yylval.name, yytext);
                            return VARIABLE;
                        }

[0-9]+         {
                    yylval.iValue = atoi(yytext);
                    return INTEGER;
                }



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