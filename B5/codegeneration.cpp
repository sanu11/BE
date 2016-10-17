#include<iostream>
#include<stdlib.h>
using namespace std;

struct bin_tree
{
	char data;
	int label;
	struct bin_tree *left,*right;
};
typedef bin_tree node;

class dag
{
	public:
	int R[10];
	int top;
	void insert(node **tree , char d)
	{
		node *temp;
		temp = (node *)malloc(sizeof(node));
		temp->data = d;
		temp->label = -1;
		*tree = temp;
		cout<<"Enter the number of child for "<<d<<" : ";
		int ch;
		cin>>ch;
		if(ch == 2)
		{
			cout<<"Enter the data of left child for "<<d<<" : ";
			char a;
			cin>>a;
			insert(&(*tree)->left,a);
			cout<<"Enter the data of right child for "<<d<<" : ";
			cin>>a;
			insert(&(*tree)->right,a);
		}
		else
			(*tree)->left = (*tree)->right = NULL;
	}
	void labelleafnode(node *tree,int val)
	{
		if(tree->left == NULL && tree->right == NULL)
			tree->label = val;
		else
		{
			labelleafnode(tree->left,1);
			labelleafnode(tree->right,0);
		}
	}
	void labelallnodes(node *tree)
	{
		if(tree->left->label == -1)
			labelallnodes(tree->left);
		if(tree->right->label == -1)
			labelallnodes(tree->right);
		if(tree->left->label == tree->right->label)
			tree->label = tree->left->label+1;
		else
			tree->label = (tree->left->label > tree->right->label ? tree->left->label : tree->right->label );
	}
	void print_inorder(node * tree)
	{
		if(tree)
		{
			print_inorder(tree->left);
			cout << tree->data <<" with Label "<< tree->label << "\n";
			print_inorder(tree->right);
		}
	}
	void initializestack(node *tree)
	{	
		int t = tree->label - 1;
		top = tree->label - 1;
		for(int i=0 ; i <= top ; i++)
		{
			R[i] = t-- ;
		}
		
	}
	void op(char x)
	{
		switch(x)
		{
			case '+' :
				cout<<"ADD ";
				break;
			case '-' :
				cout<<"SUB ";
				break;
			case '*' :
				cout<<"MUL ";
				break;
			case '/' :
				cout<<"DIV ";
				break;
		}
	}
	void generatecode(node *tree)
	{
		if(tree->left != NULL && tree->right != NULL)
		{
			if(tree->left->label == 1 && tree->right->label == 0)
			{
				cout<<"MOV R["<<R[top]<<"],"<<tree->left->data<<endl;
				op(tree->data);
				cout<<"R["<<R[top]<<"],"<<tree->right->data<<endl;
			}
			else if(tree->left->label >= tree->right->label )
			{	
				generatecode(tree->left);
				top--;
				generatecode(tree->right);
				top++;
				op(tree->data);
				cout<<"R["<<R[top]<<"],R["<<R[top-1]<<"]\n";
			}
			else if(tree->left->label >= 1 && tree->right->label == 0)
			{	
				int temp= R[0];
				R[0] = R[1];
				R[1] = temp;
				generatecode(tree->right);
				top--;
				generatecode(tree->left);
				top++;
				temp= R[0];
				R[0] = R[1];
				R[1] = temp;
				op(tree->data);
				cout<<"R["<<R[top]<<"],R["<<R[top-1]<<"]\n";
			}
			else if(tree->left->label >= 1 && tree->right->label == 0)
			{
				generatecode(tree->left);
				op(tree->data);
				cout<<"R["<<R[top]<<"],"<<tree->right->data<<endl;
			}
		}
		else
			cout<<"MOV R["<<R[top]<<"],"<<tree->data<<endl;
	}
};

int main()
{
	node *root = NULL;
	char val;
	cout<<"Enter the root value : ";
	cin>>val;
	dag d;
	d.insert(&root,val);
	d.labelleafnode(root,1);
	d.labelallnodes(root);
	d.initializestack(root);
	d.print_inorder(root);
	d.generatecode(root);
	return 0;
}
