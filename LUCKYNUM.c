#include <stdio.h>

int main(void) {
	// your code goes here
	int test_case;
	scanf("%d",&test_case);
	int a,b,c;
	for(int i=0;i<test_case;i++){
	    scanf("%d%d%d",&a,&b,&c);
	    if(a==7||b==7||c==7){
	        printf("YES\n");
	    }
	    else{
	        printf("NO\n");
	    }
	}
	return 0;
}
