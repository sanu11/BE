#include<bits/stdc++.h>
using namespace std;
string input;
int i=0;
bool error=false;
void E();
void T();
void Tdash();
void Edash(	);
void F();
int main()
{
	cin>>input;
	E();
	if(input.length()==i&&!error)
		cout<<"String is Accepted"<<endl;
	else
		cout<<"String is not Accepted"<<endl;

	
}


void E()
{
	T();
	Edash();

}
void Edash()
{

	if(input[i]=='+')
	{
		i++;
		T();
		Edash();
	}
	
}
void T()
{
	F();
	Tdash();

}
void Tdash()
{
	if(input[i]=='*')
	{
		i++;
		F();
		Tdash();
	}	

}
void F()
{
	if(isalnum(input[i]))
		i++;
	else if(input[i]=='(')
	{
		i++;
		E();
		if(input[i]==')')
			i++;
		else 
			error=true;
	}
	else
		error=true;

}
