%{

#include "y.tab.h"

%}

%%
main                {return MAIN;};
printf              {return PRINT;};
if 		    {return IF;};
else		    {return ELSE;};
for		    {return FOR;};

\+\+|\-\-	    {return INC;};
=		    {return ASSIGNMENT;};
[0-9]+		    {return NUM;};
\<\=|\>\=|\=\=|\!\=|\>|\<  {return RELOP;}; 
int|float|char     {return DATATYPE;};
[a-zA-Z]+          {return IDENTIFIER;};
\"[a-zA-Z0-9]*\"   {return STCONST;}; 
[ \n\t]+         	;
.                  {return yytext[0];};

%%
int yywrap()
{

	return 1;

}

