%{
#include <stdio.h>
%}

%%
begin  printf("Started\n");
hello  printf("Hello yourself!\n");
thanks printf("You are welcome\n");
end    printf("Stopped\n");
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