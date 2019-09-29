#include <stdio.h>
#include <stdlib.h>

void win()
{
	char flag[256];
	FILE* f = fopen("./flag.txt", "r");
	if (f == NULL)
	{
		puts("flag.txt not found - ping us on discord if this is happening on the shell server\n");
		exit(1);
	}
	else
	{
		fgets(flag, sizeof(flag), f);
		puts(flag);
	}
}

void vuln(int* num)
{
	char buf[64];
	printf("Type something>");
	fgets(buf, sizeof(buf), stdin);
	printf("You typed: ");
	printf(buf);
}

int main()
{
	/* Disable buffering on stdout */
	setvbuf(stdout, NULL, _IONBF, 0);

	int num = 0;

	vuln(&num);

	if (num == 42)
	{
		puts("You win!");
		win();
	}
	else
	{
		printf("%d != 42, try again", num);
	}

	return 0;
}
