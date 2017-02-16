#include <stdio.h>

int main()
{
	int S;
	FILE *f = fopen("input.txt", "r");
	fscanf(f, "%d", &S);
	fclose(f);

	int nums[1002];
	for(int a = 1, b = 1, c = 1; a<1000; c = a + b, a = b, b = c)
	{
		if(c>1000)
			c = 1001;
		for(int t = a+1; t<c; ++t)
			nums[t] = nums[t-a] + 1;
		nums[c] = 1;
	}

	f = fopen("output.txt", "w");
	fprintf(f, "%d\n", nums[S]+1);
	fclose(f);
	return 0;
}