#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void)
{
	srand(time(NULL));
	int r = rand();
	char url[90] = "nc3ctffqqn5ozfjy.onion/";
	printf("23/09/90 kl. 01:12:12 UTC er det helt rigtige unix-tidspunkt til at skabe en URL\n");
	printf("%s%d\n", url, r);
	return(0);
}
