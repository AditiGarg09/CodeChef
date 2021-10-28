#include <stdio.h>

int main(void) {
	// your code goes here
	int testcase,n,x,p,remainingQues,correctScore,finalScore;
	scanf("%d",&testcase);
	
	for(int i=0;i<testcase;i++){
	    scanf("%d%d%d",&n,&x,&p);
	    
	    correctScore=x*3;
	    remainingQues=n-x;
	    finalScore=correctScore-remainingQues;
	    
	    if(finalScore>=p){
	        printf("PASS\n");
	    }
	    else{
	        printf("FAIL\n");
	    }
	}
	return 0;
}
