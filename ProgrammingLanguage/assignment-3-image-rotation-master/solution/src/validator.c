#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "validator.h"

static char *ErrorValidation[] = {
        "Everything is OK",
        "Number of args != 4",
        "ANGLE IS NOT ALLOWED (0, 90, -90, 180, -180, 270, -270)"
};

enum validation_results valid_arg(int argc, char** argv, char** source_image, char** source_rotated_image, int* angle){
    int value;

    if ( argc != 4){
        return ERROR_ARGC;
    }
    *source_image = argv[1];
    *source_rotated_image = argv[2];
    if (argv[3][0] == '-')
    {
        for (int i = 1; i < strlen(argv[3]); i++){
            if (!isdigit(argv[3][i]))
                return ERROR_ANGLE;
        }
    } else {
        for (int i = 0; i < strlen(argv[3]); i++){
            if (!isdigit(argv[3][i]))
                return ERROR_ANGLE;
        }
    }


    value = atoi(argv[3]);
    while (value < 0) {
        value += 360;
    }
    value %= 360;
    *angle = value;

    return NORM;
}


void print_error_validation(enum validation_results res){
    printf("%s", ErrorValidation[res]);
}
