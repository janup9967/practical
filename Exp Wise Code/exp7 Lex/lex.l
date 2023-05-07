%{
int COMMENT=0;
%}
identifier [a-zA-Z][a-zA-Z0-9]*
%%
#.* {printf("\n%s is a preprocessor directive",yytext);}
int |
float |
char |
double |
while |
for |
struct |
typedef |
do |
if |
break |
continue |
void |
switch |
return |
else |
goto {printf("\n\t%s is a keyword",yytext);}
"/*" {COMMENT=1;}{printf("\n\t %s is a COMMENT",yytext);}
{identifier}\( {if(!COMMENT)printf("\nFUNCTION \n\t%s",yytext);}
\{  {if(!COMMENT)printf("\n BLOCK BEGINS");}
\}  {if(!COMMENT)printf("BLOCK ENDS ");}
{identifier}(\[[0-9]*\])? {if(!COMMENT) printf("\n %s IDENTIFIER",yytext);}
\".*\" {if(!COMMENT)printf("\n\t %s is a STRING",yytext);}
[0-9]+ {if(!COMMENT) printf("\n %s is a NUMBER ",yytext);}
\)(\:)? {if(!COMMENT)printf("\n\t");ECHO;printf("\n");}
\( ECHO;
= {if(!COMMENT)printf("\n\t %s is an ASSIGNMENT OPERATOR",yytext);}
\<= |
\>= |
\< |
== |
\> {if(!COMMENT) printf("\n\t%s is a RELATIONAL OPERATOR",yytext);}
%%
int main(int argc, char **argv)
{
FILE *file;
file=fopen("var.c","r");
if(!file)
{
printf("could not open the file");
exit(0);
}
yyin=file;
yylex();
printf("\n");
return(0);
}
int yywrap()
{
return(1);
}


Another 

%{
	#define NUM 1
	#define KEY 2
	#define ID 3
	#define DEC 4
%}

%%
[0-9]+ {return NUM;}
int|char|float|return {return KEY;}
[a-zA-Z]+[a-zA-Z0-9]* {return ID;}
[0-9]+\.[0-9]+ {return DEC;}
%%

#include<stdio.h>
int yywrap(){}
int main(int argc, char *argv[])
	{
		int val;
		while(val=yylex())
		{
			switch(val){
				case 1: printf("\n %s Number", yytext);
						break;
				case 2: printf("\n %s Key", yytext);
						break;
				case 3: printf("\n &s Id", yytext);
						break;
				case 4: printf("\n %s Decimal",yytext);
						break;
				default: printf("error");
			}
		}
	}
