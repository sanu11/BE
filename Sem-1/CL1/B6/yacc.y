%{
#include<stdio.h>

typedef struct node
{
	struct node *left;
	struct node *right;
	char *token;
}node;
node* mknode(node* left,char* token,node* right);
void printtree(node* root);
#define YYSTYPE struct node *

%}

%start lines

%token NUMBER PLUS MINUS DIVIDE TIMES POWER  OPEN CLOSE END

%left	PLUS MINUS
%left   TIMES DIVIDE
%right POWER


%%

lines: line lines | line |  		               ;

line : expr END                                        {  printtree($1);printf("\n");return 0; }
	;

expr : term  				               {  $$ = $1;}
       | expr PLUS term  		               {  $$ = mknode($1 , "+" , $3);}
       | expr MINUS term 			       {  $$ = mknode($1 , "-" , $3);}
       ;

term : fact  				               {  $$ = $1 ;}
       | fact TIMES term		      	       {  $$ = mknode($1 , "*" , $3);}
       | fact DIVIDE term			       {  $$ = mknode($1 , "/" , $3);}
       ;
       
fact: NUMBER	                   	               {  $$ = mknode(0 , (char*)yylval, 0);}
      | OPEN expr CLOSE			               {  $$ = $2; }
      ;

%% 

void main()
{
yyparse();

}
void printtree(node* root)
{
	if(root->left || root->right)
		printf(" ( ");
	printf(" %s ",root->token);
	if(root->left)
		printtree(root->left);
	if(root->right)
		printtree(root->right);
	if(root->left || root->right)
	printf(" ) ");	

}

node* mknode(node* left,char* token,node* right)
{
	node* newnode=(node*)malloc(sizeof(node));
	char *str = (char*)malloc(sizeof(strlen(token)+1));
	newnode->left=left;
	newnode->right=right;
	strcpy(str, token);
	newnode->token=str;
	return newnode;
}
yyerror()
{
printf("Syntax Error\n");
}

