%{
#include<stdio.h>
#include<string.h>

FILE *opfile;
int lno=1;
int error=0;
char error_desc[20][100];
int id_cnt=0;
int arr_line[20];
char name[30][100];

%}

%%
#  {  printf("%d		%s		PREPROCESSOR\n",lno , yytext) ; fprintf(opfile,"%s " , yytext);}
[a-zA-Z0-9]+\.h	{  printf("%d		%s		HEADER\n",lno , yytext) ; fprintf(opfile,"%s " , yytext);}
include|return|break|main|while|continue|if|for {  printf("%d %s KEYWORD\n" ,lno , yytext) ; fprintf(opfile,"%s " , yytext);}

int|float|char|double  { printf("%d 		%s 		DATATYPE\n",lno , yytext) ; fprintf(opfile,"%s " , yytext);}


scanf|printf  { printf("%d %s  LIBRARY FUNCTIONS\n",lno , yytext) ; fprintf(opfile,"%s " , yytext);}

\"[a-zA-Z0-9]*\"	{ printf("%d		 %s 		STRING CONST\n",lno , yytext) ; fprintf(opfile,"%s " , yytext);  }
[a-zA-Z][a-zA-Z0-9]*  { printf("%d		 %s 		IDENTIFIER\n",lno , yytext) ; fprintf(opfile,"%s " , yytext); add_identifier(yytext);}
[0-9]+[a-zA-Z]+	{ printf("%d		 %s 		 UNRECOGNISED IDENTIFIER\n",lno , yytext) ; fprintf(opfile,"%s " , yytext); char str[100]="Unrecognised Token " ;strcat(str,yytext); arr_line[error]=lno; strcpy(error_desc[error],str);error++; }

[a-zA-Z]+[?/@$][a-zA-Z0-9]	{ printf("%d		 %s		 UNRECOGNISED IDENTIFIER\n",lno , yytext) ; fprintf(opfile,"%s " , yytext);}

[0-9]+  {  printf("%d %s NUMBER\n",lno , yytext) ; fprintf(opfile,"%s " , yytext);}

;	{ printf("%d    	  %s  	         TERMINATOR\n",lno , yytext) ; fprintf(opfile,"%s " , yytext);}
=	{ printf("%d    	  %s	           ASSIGNMENT\n",lno , yytext) ; fprintf(opfile,"%s " , yytext);}
,	{ printf("%d   		  %s    	       	SEPARATOR\n",lno , yytext) ; fprintf(opfile,"%s " , yytext);} 	
\{	{ printf("%d   		  %s      	     OPEN BLOCK\n",lno , yytext) ; fprintf(opfile,"%s " , yytext);}
\}	{ printf("%d    	  %s    	       CLOSE BLOCK\n",lno , yytext) ; fprintf(opfile,"%s " , yytext);}	
\(	{ printf("%d     	 %s  	         OPEN BRACE\n",lno , yytext) ; fprintf(opfile,"%s " , yytext);}
\)	{ printf("%d    	  %s      	     CLOSE BRACE\n",lno , yytext) ; fprintf(opfile,"%s " , yytext);}
\<	{ printf("%d    	  %s           LESS THAN\n",lno , yytext) ; fprintf(opfile,"%s " , yytext);}	
\>	{ printf("%d   	          %s           GREATER THAN\n" ,lno , yytext) ; fprintf(opfile,"%s " , yytext);}

\n {fprintf(opfile,"\n");lno++;}
[\t]	 ;

%%

main()
{
	int i;
	char infile[100];
	printf("Enter input file name	");
	scanf("%s",infile);


	char ofile[100];
	printf("Enter output file name	");
	scanf("%s",ofile);
	
	opfile=fopen(ofile,"w");

	yyin=fopen(infile,"r");

	printf("Line no      LEXEME   	  Token\n");
	yylex();


	printf("Symbol Table %d " ,id_cnt);

		
	for( i=0;i<id_cnt;i++)
	{
		printf(" \n %s \n",name[i]);

	}


	printf("Lexical error found %d" ,error);
	printf("\nLine NO      Error\n");
	for( i=0;i<error;i++)
	{

	printf("%d %s\n  ",arr_line[i] , error_desc[i]);

	}
	return 0;

}

void add_identifier(char s[50])
{
	int i;
	for(i=0;i<id_cnt;i++)
	{
		if(strcmp(name[i],s)==0)
			return;

	}
			
		strcpy(name[id_cnt],s);
		id_cnt++;
}

int yywrap()
{

	return 1;
}
