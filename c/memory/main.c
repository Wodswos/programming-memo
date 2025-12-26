#include <stdio.h>
#include <stdlib.h> // 用于 exit()

int main() {
    FILE *fp;
    char *filename = "example.txt";
    
    fp = fopen(filename, "w");

    if (fp == NULL) {
        perror("Error opening file"); // 打印错误信息
        return EXIT_FAILURE;
    }

    fputs("This is the first line.\n", fp); 
    int year = 2025;
    fprintf(fp, "The current year is %d.\n", year);

    if (fclose(fp) == 0) {
        printf("Successfully wrote data to %s and closed the file.\n", filename);
    } else {
        perror("Error closing file");
    }

    return EXIT_SUCCESS;
}