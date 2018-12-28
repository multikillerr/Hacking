#include<stdio.h>
#include<string.h>
int main(int argc, char *argv[]){
	if(argc==2){
		int sum=0,i;
		for(i=0;i<strlen(argv[1]);i++){
			sum+=(int)argv[1][i];
		}if(sum==916){
			printf("Access Granted");
		}else{
			printf("WRONG!");
		}
	}else{
		printf("WRONG USAGE!");
	}
}
