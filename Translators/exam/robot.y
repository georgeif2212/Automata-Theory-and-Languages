%{
#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>
#include "robot_header.h"
#include "lex.yy.c"
#include "Maze.h"

/* prototypes */
nodeType *opr(int oper, int nops, ...);
nodeType *id(int i);
nodeType *con(int value);
void freeNode(nodeType *p);
int ex(nodeType *p);

int sym[26]; /* Tabla de símbolos */
MazeSimulator mazeSimulator;
%}

/* Declaración de Yacc que generará una Unión en C */
%union {
    int iValue;                 /* Valor entero */
    int sIndex;                /* Índice de la tabla de símbolos */
    nodeType *nPtr;             /* Apuntador a nodo */
};

%token <iValue> INTEGER
%token <sIndex> VARIABLE
%token IF WHILE PRINT DO MOVE TURNLEFT ISWALL START END TURNOFF AND OR
%nonassoc IFX
%nonassoc ELSE

%left GE LE EQ NE '>' '<' NO
%left '+' '-'
%left '*' '/' '%'
%nonassoc UMINUS

%type <nPtr> stmt expr stmt_list

%%

program:
         function '.'      { exit(0); }
         ;

function:
         function stmt     { ex($2); freeNode($2); }
         | /* NULL */
         ;

stmt:
         ';'                                   { $$ = opr(';', 2, NULL, NULL); }
         | expr ';'                            { $$ = $1; }
         | PRINT  expr ';'                     { $$ = opr(PRINT, 1, $2); }
         | VARIABLE '=' expr ';'               { $$ = opr('=', 2, id($1), $3); }
         | MOVE ';'                            { $$ = opr(MOVE, 0); }
         | TURNLEFT                            { $$ = opr(TURNLEFT, 0); }
         | WHILE expr DO START stmt_list END   { $$ = opr(WHILE, 2, $2, $5); }
         | TURNOFF                             { $$ = opr(TURNOFF, 0); }
         | IF '(' expr ')' stmt %prec IFX      { $$ = opr(IF, 2, $3, $5); }
         | IF '(' expr ')' stmt ELSE stmt      { $$ = opr(IF, 3, $3, $5, $7); }
         | '{' stmt_list '}'                   { $$ = $2; }
         ;

stmt_list:
         stmt                    { $$ = $1; }
         | stmt_list stmt        { $$ = opr(';', 2, $1, $2); }
         ;

expr:
         INTEGER                 { $$ = con($1); }
         | VARIABLE        		{ $$ = id($1); }
         | '-' expr %prec UMINUS { $$ = opr(UMINUS, 1, $2); }
         | expr '+' expr         { $$ = opr('+', 2, $1, $3); }
         | expr '-' expr         { $$ = opr('-', 2, $1, $3); }
         | expr '*' expr         { $$ = opr('*', 2, $1, $3); }
         | expr '/' expr         { $$ = opr('/', 2, $1, $3); }
         | expr '<' expr         { $$ = opr('<', 2, $1, $3); }
         | expr '>' expr         { $$ = opr('>', 2, $1, $3); }
         | expr GE expr          { $$ = opr(GE, 2, $1, $3); }
         | expr LE expr          { $$ = opr(LE, 2, $1, $3); }
         | expr NE expr          { $$ = opr(NE, 2, $1, $3); }
         | expr EQ expr          { $$ = opr(EQ, 2, $1, $3); }
         | expr AND expr         { $$ = opr(AND, 2, $1, $3); }
         | expr OR expr          { $$ = opr(OR, 2, $1, $3); }
         | ISWALL                { $$ = opr(ISWALL, 0); }
         | NO expr               { $$ = opr(NO, 1, $2); }
         | '(' expr ')'          { $$ = $2; }
         ;

%%


nodeType *con(int value) {
   nodeType *p;

   /* allocate node */
   if ((p = (nodeType*) malloc(sizeof(conNodeType))) == NULL)
      yyerror("out of memory");

   /* copy information */
   p->type = typeCon;
   p->con.value = value;

   return p;
}

nodeType *id(int i) {
   nodeType *p;

   /* allocate node */
   if ((p = (nodeType*) malloc(sizeof(conNodeType))) == NULL)
      yyerror("out of memory");

   /* copy information */
   p->type = typeId;
   p->id.i = i;

   return p;
}

nodeType *opr(int oper, int nops, ...) {
   va_list ap;
   nodeType *p;
   size_t size;
   int i;

   /* allocate node */
   size = sizeof(oprNodeType) + (nops-1) * sizeof(nodeType*);
   if ((p = (nodeType*) malloc(size)) == NULL)
      yyerror("out of memory");

   /* copy information */
   p->type = typeOpr;
   p->opr.oper = oper;
   p->opr.nops = nops;
   va_start(ap, nops);
   for (i = 0; i < nops; i++)
      p->opr.op[i] = va_arg(ap, nodeType*);
   va_end(ap);
   return p;
}

void freeNode(nodeType *p) {
   int i;

   if (!p) return;
   if (p->type == typeOpr) {
      for (i = 0; i < p->opr.nops; i++)
         freeNode(p->opr.op[i]);
   }
   free (p);
}


int ex(nodeType *p) {

   if (!p) return 0;

   switch(p->type) {
      case typeCon: return p->con.value;
      case typeId : return sym[p->id.i];
      case typeOpr: 
         switch(p->opr.oper) {
            case WHILE: while(ex(p->opr.op[0]))
                           ex(p->opr.op[1]);
                        return 0;
            case IF: if (ex(p->opr.op[0]))
                        ex(p->opr.op[1]);
                     return 0;
            case MOVE: mazeSimulator.drawMaze();
                        mazeSimulator.moveRobot();
                        printf("movimiento\n");
                        return 0;
            case ISWALL: return mazeSimulator.wallAhead();

            case NO:    return !ex(p->opr.op[0]);
            case TURNLEFT: mazeSimulator.turnRobot(-1);
                        return 0;
            case TURNOFF:printf("SE TERMINÓ EL PROGRAMA\n");
                        return 0;
            case PRINT: printf("%d\n", ex(p->opr.op[0]));
                        return 0;
            case ';':   ex(p->opr.op[0]);
                        return ex(p->opr.op[1]);
            case '=':   return sym[p->opr.op[0]->id.i] = ex(p->opr.op[1]);
            case UMINUS: return -ex(p->opr.op[0]);
            case '+': return ex(p->opr.op[0]) + ex(p->opr.op[1]);
            case '-': return ex(p->opr.op[0]) - ex(p->opr.op[1]);
            case '*': return ex(p->opr.op[0]) * ex(p->opr.op[1]);
            case '/': return ex(p->opr.op[0]) / ex(p->opr.op[1]);
            case '<': return ex(p->opr.op[0]) < ex(p->opr.op[1]);
            case '>': return ex(p->opr.op[0]) > ex(p->opr.op[1]);
            case GE: return ex(p->opr.op[0]) >= ex(p->opr.op[1]);
            case LE: return ex(p->opr.op[0]) <= ex(p->opr.op[1]);
            case NE: return ex(p->opr.op[0]) != ex(p->opr.op[1]);
            case EQ: return ex(p->opr.op[0]) == ex(p->opr.op[1]);
            case AND: return ex(p->opr.op[0]) && ex(p->opr.op[1]);
            case OR:  return ex(p->opr.op[0]) || ex(p->opr.op[1]);
         }
   }
   return 0;
}

int main(int argc, char **argv) {
   extern FILE* yyin;
   mazeSimulator.drawMaze();
   yyin = fopen(argv[1], "r");
   yyparse();
   return 0;
}