%{
#include <stdlib.h>
//#include "casio_plus.h"
#include "y.tab.h"

int yyerror( char *s );
int yylex();
int yywrap();

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



[ \t\n+]    ;       /* ignore whitespace */

.           yyerror("token no reconocido.");

%%

int yyerror( char *s ) { fprintf( stderr, "%s\n", s); }

int yywrap(void) {
    return 1;
}