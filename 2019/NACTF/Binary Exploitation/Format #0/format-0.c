#include <stdio.h>
#include <stdlib.h>

void vuln(char* flag)
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
	}
	vuln(flag);

	return 0;
}
