#include <stdio.h>
#include <stdlib.h>

void win(long long arg1, int arg2)
{
	if (arg1 != 0x14B4DA55 || arg2 != 0xF00DB4BE)
	{
		puts("Close, but not quite.");
		exit(1);
	}

	printf("You win!\n");
	char buf[256];
	FILE* f = fopen("./flag.txt", "r");
	if (f == NULL)
	{
		puts("flag.txt not found - ping us on discord if this is happening on the shell server\n");
	}
	else
	{
		fgets(buf, sizeof(buf), f);
		printf("flag: %s\n", buf);
	}
}

void vuln()
{
	char buf[16];
	printf("Type something>");
	gets(buf);
	printf("You typed %s!\n", buf);
}

int main()
{
	/* Disable buffering on stdout */
	setvbuf(stdout, NULL, _IONBF, 0);

	vuln();
	return 0;
}
