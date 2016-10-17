%{

#include<stdio.h>

%}

%token MAIN DATATYPE IDENTIFIER PRINT STCONST IF ELSE FOR RELOP NUM OP ASSIGNMENT INC

%%
main:MAIN '('')' '{' body '}'                   {printf("Valid main\n");};

body:state body|;
state:vardec | printf | if | else | for ;
printf: PRINT '(' STCONST ')' ';'               {printf("Valid print\n");};
vardec:DATATYPE varlist ';' ;
varlist: IDENTIFIER  ',' varlist | IDENTIFIER     {printf("Valid declaration\n");};
if: IF '(' condition ')' '{' body '}'  { printf("Valid if\n"); };
condition: IDENTIFIER RELOP var;
var:NUM|IDENTIFIER;
else : ELSE '{' body '}' {printf("Valid else\n");};
 
for:  FOR '(' for1 ';' for2 ';'for3 ')' '{' body '}'    {printf("Valid for\n");};
for1: DATATYPE assg | ;
assg: IDENTIFIER ASSIGNMENT var ','  assg | IDENTIFIER ASSIGNMENT var  ;
for2: IDENTIFIER RELOP var | IDENTIFIER RELOP var ',' for2  |;
for3: IDENTIFIER INC| IDENTIFIER INC ',' for3   |;

%%
extern FILE *yyin;
main()
{

	yyin=fopen("input.txt","r");
	yyparse();

}

yyerror()
{

	printf("invalid syntax");

}

