#include <stdio.h>

int main(void) {
	// your code goes here
	int testcase;
	scanf("%d",&testcase);
	
	int arr[5];
	
	for(int j=0;j<testcase;j++){
    	for(int i=0;i<5;i++){
    	    scanf("%d",&arr[i]);
    	}
    	
    	int IndiaWin=0;
    	int EnglandWin=0;
    	
    	for(int i=0;i<5;i++){
    	    if(arr[i]==1){
    	        IndiaWin++;
    	    }
    	    else if(arr[i]==2){
    	        EnglandWin++;
    	    }
    	}
    	
    	if(IndiaWin==EnglandWin){
    	    printf("Draw\n");
    	}
    	else if(IndiaWin>EnglandWin){
    	    printf("India\n");
    	}
    	else{
    	    printf("England\n");
    	}
	}
	return 0;
}
