%{
#include "y.tab.h"
%}

%%

[ \n\t] ;
[0-9]+	{ yylval =(int)yytext ;return NUMBER;};
"+"	{return PLUS;};
"-"	{return MINUS;};
"/"	{return DIVIDE;};
"*"	{return TIMES;};
"^"	{return POWER;};	
";"	{return END;};
"("	{return OPEN;};
")"	{return CLOSE;};

%%
int yywrap(){return 1;}
