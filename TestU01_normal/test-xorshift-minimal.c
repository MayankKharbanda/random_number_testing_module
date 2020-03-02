// Adapted from TestU01 manual, Figure 2.2, Figure 2.4

#include "TestU01.h"
#include<time.h>
#include <stdio.h> 
#include <stdlib.h> 

// Example PRNG: Xorshift 32

static unsigned int y = 2463534242U;

unsigned int xorshift (void)
{
    FILE *fp1;    
    fp1=fopen("python_random_testu01.bin","rb");
    unsigned int x;
    char str[60];
    for(unsigned long i=0;i<p;i++)
    	fgets(str, 60, fp1);
    if(fgets(str, 60, fp1)!=NULL)
    {
    	sscanf(str,"%u",&x);
    	//printf("%u\n",x);
    	if(p < 4294967290)
    	    p++;
    	else
    		p=0;
    }
    else{
    	fseek(fp1,0,SEEK_SET);
    	fgets(str, 60, fp1);
    	sscanf(str,"%u",&x);
    	p=0;
    	p++;
    }
	fclose(fp1);
    return x;
    srand(time(0));
    return rand();
}

int main()
{
    // Create TestU01 PRNG object for our generator
    unif01_Gen* gen = unif01_CreateExternGenBits("Xorshift 32", xorshift);

    // Run the tests.
    bbattery_SmallCrush(gen);

    // Clean up.
    unif01_DeleteExternGenBits(gen);

    return 0;
}
