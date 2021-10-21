#include <stdio.h>

int main(void) {
	// your code goes here
	int x;
	float totalBal;
	scanf("%d%f",&x,&totalBal);
	
	if((x+0.50<=totalBal) && (x%5==0)){
	    totalBal=totalBal-x-0.50;
	}
	printf("%.2f",totalBal);
	return 0;
}
