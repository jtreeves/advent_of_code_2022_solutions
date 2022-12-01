#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    FILE* ptr;
    char ch;
 
    ptr = fopen("data.txt", "r");
 
    do {
        ch = fgetc(ptr);
        printf("%c", ch);
    } while (ch != EOF);
 
    fclose(ptr);
    
    return 0;
}
