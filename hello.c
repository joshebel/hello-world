#include <stdio.h>
#include <string.h>

/* INTENTIONAL VULNERABILITY for code-scanner testing.
 * CWE-120 / CWE-121: classic stack buffer overflow via unbounded strcpy.
 * Do not use this pattern in real software.
 * Here is an update again again
 */
void greet(char *name) {
    char buffer[16];
    strcpy(buffer, name);
    printf("Hello, %s!\n", buffer);
}

int main(int argc, char **argv) {
    if (argc < 2) {
        printf("Hello, World!\n");
        return 0;
    }
    greet(argv[1]);
    return 0;
}
