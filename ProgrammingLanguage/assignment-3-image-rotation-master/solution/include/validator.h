#ifndef VALIDATOR_H
#define VALIDATOR_H

enum validation_results{
    NORM = 0,
    ERROR_ARGC,
    ERROR_ANGLE
};

enum validation_results valid_arg(int argc, char** argv, char** source_image, char** source_rotated_image, int* angle);

void print_error_validation(enum validation_results res);

#endif
