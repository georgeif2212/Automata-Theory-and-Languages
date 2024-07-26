/*Definimos el nombre de la gramática*/
grammar Ejemplo;

/*Definimos la gramática*/
programa: sentencia*;

sentencia: expresion';' | asignacion';' | funcion';';

expresion: expresion OPERADORES expresion | NUMERO;

asignacion:  VARIABLE '=' NUMERO | VARIABLE '=' VARIABLE;

funcion: VARIABLE '('argumentos')';

argumentos: NUMERO | STRINGS | VARIABLE;

ESPACIOS: [ \n\t\r]+ -> skip;
OPERADORES: '+' | '*';
NUMERO: [0-9]+;
STRINGS: '"'[ a-zA-Z0-9:]*'"';
VARIABLE: [a-zA-Z][a-zA-Z0-9]*;