#include<stdio.h>
int main()
{
	int v1,v2;
	printf("Please enter the number\n");
	scanf("%d%d",&v1,&v2);
	v2+=v1;
		printf("v2 is :%d\n",v2);
	v2-=v1;
		printf("v2 is :%d\n",v2);
	v1*=v1;
		printf("v1 is :%d\n",v1);
	v2/=10;
		printf("v2 is :%d\n",v2);
	v1%=10;
		printf("v1 is :%d\n",v1);
}
