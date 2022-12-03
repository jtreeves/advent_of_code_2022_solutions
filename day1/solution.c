#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    FILE* ptr;
    char ch;
    char file_contents[10000000] = "";
 
    ptr = fopen("data.txt", "r");
 
    do {
        ch = fgetc(ptr);
        strncat(file_contents, &ch, 1);
        // printf("%c", ch);
    } while (ch != EOF);
 
    printf("%s", file_contents);
    fclose(ptr);
    
    return 0;
}
