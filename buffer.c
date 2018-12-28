#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
#include<string.h>
void win(){
	printf("Code Overflow ");
}
int main(int argc, char **argv){
	volatile int(*fp)();
	char buffer[64];
	fp=0;
	gets(buffer);
	if(fp){
		printf("Calling function pointer, jumping to 0x%08x\n",fp);
		fp();
	}
}
