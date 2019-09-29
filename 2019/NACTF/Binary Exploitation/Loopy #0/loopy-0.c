#include <stdio.h>

void vuln()
{
	char buf[64];
	fputs("Type something>", stdout);
	gets(buf);
	fputs("You typed: ", stdout);
	printf(buf);
}

int main()
{
	/* Disable buffering on stdout */
	setvbuf(stdout, NULL, _IONBF, 0);

	vuln();

	return 0;
}
