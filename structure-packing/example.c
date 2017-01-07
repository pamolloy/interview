/*
 * example.c - Example of structure packing
 */

#include <stdio.h>      // printf
#include <stddef.h>     // offsetof
#include <stdlib.h>     // exit
#include <stdbool.h>

int main(int argc, char *argv[])
{
    struct start_pad {
        char c;     // 1 byte
        char *p;    // 8 bytes on a 32-bit machine
        long l;     // 8 bytes
    } start;
    printf("offsetof(start_pad, c) %i\n", offsetof(struct start_pad, c));
    printf("offsetof(start_pad, p) %i\n", offsetof(struct start_pad, p));
    printf("sizeof(start) %i\n", sizeof(start));

    struct center_pad {
        char *p;    // 8 bytes on a 64-bit machine
        char c;     // 1 byte
        long l;     // 8 bytes
    } center;
    printf("offsetof(center_pad, p) %i\n", offsetof(struct center_pad, p));
    printf("offsetof(center_pad, c) %i\n", offsetof(struct center_pad, c));
    printf("sizeof(center) %i\n", sizeof(center));

    struct {
        char *p;    // 8 bytes on a 64-bit machine
        long l;     // 8 bytes
        char c;     // 1 byte
    } trailing;
    printf("sizeof(trailing) %i\n", sizeof(trailing));

    struct {
        struct {
            char *p;    // 8 bytes on a 64-bit machine
        } inner;
        char c;     // 1 byte
    } nested;
    printf("sizeof(nested) %i\n", sizeof(nested));

    struct {
        char c;     // 1 byte
        char *p;    // 8 bytes on a 64-bit machine
        short s;    // 2 bytes
    } unordered;
    printf("sizeof(unordered) %i\n", sizeof(unordered));

    struct {
        char *p;    // 8 bytes on a 64-bit machine
        short s;    // 2 bytes
        char c;     // 1 byte
    } ordered;
    printf("sizeof(ordered) %i\n", sizeof(ordered));

    exit(EXIT_SUCCESS);
}
