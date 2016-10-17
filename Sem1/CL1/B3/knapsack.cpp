#include<bits/stdc++.h>
using namespace std;
class item;
int n,w;
item *arr;
class item
{
public:
	float weight;
	int value;
	void set(float weight,int value)
	{
		this->weight=weight;
		this->value=value;
	}
};

class node
{
public:
	int upper_bound;
	int profit;
	float tot_wt;
	int level;

};
bool cmp(item a,item b)
{
	double r1 = (double) (a.value/a.weight);
	double r2 = (double) (b.value/b.weight);
	return r1>r2;

}
int bound(node v)
{
	int level=v.level;
	level+=1;
	int total=v.tot_wt;

	int temp;
	int upp_bnd=v.profit;
	while(level<n && (total+arr[level].weight)<=w)
	{
		
			total+=arr[level].weight;
			upp_bnd+=arr[level].value;
			level++;

	}
	if(level<n)
	{

		int wt_let=(w-total);
		int val_per_wt = (arr[level].value /arr[level].weight);
		upp_bnd+=wt_let*val_per_wt;

	}
	return upp_bnd;


}


int knapsack()
{
	sort(arr,arr+n,cmp);
	queue<node>q;
	node u,v;
	u.level=-1;
	u.tot_wt=0;
	u.profit=0;
	q.push(u);
	int mxprofit=0;
	while(!q.empty())
	{
		u=q.front();
		q.pop();
		if(u.level==n-1)
			continue;

		v.level=u.level+1;
		//include item

		v.tot_wt=u.tot_wt + arr[v.level].weight;
		v.profit=u.profit + arr[v.level].value;

		if(v.profit>mxprofit&&v.tot_wt<=w)
			mxprofit=v.profit;

		int upp_bnd= bound(v);

		if(upp_bnd>mxprofit)
			q.push(v);

		//dont include item;

		v.tot_wt=u.tot_wt;
		v.profit=u.profit;
		upp_bnd= bound(v);

		if(upp_bnd>mxprofit)
			q.push(v);

	}
	return mxprofit;

}

int main()
{
	cout<<"Enter number of items"<<endl;
	cin>>n;
	int val;
	float wt;
	arr=new item[n];
	cout<<"Enter weight and value of items ( space separated )"<<endl;
	for(int i=0;i<n;i++)
	{
		cin>>wt>>val;
		arr[i].set(wt,val);
	}
	cout<<"Enter Total Weight"<<endl;
	cin>>w;

	int mx=knapsack();
	cout<<mx<<endl;
	return 0;
}