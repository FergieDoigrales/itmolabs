#include <stdio.h>
#include <stdlib.h>

#include "transformation.h"
#include "fromto.h"
#include "validator.h"

int main( int argc, char** argv ) {
    int result, angle;
    struct image picture, rotated_image;
    char *source_image = "", *source_rotated_image = "";

    result = valid_arg(argc, argv, &source_image, &source_rotated_image, &angle);
    if (result != NORM){
        print_error_validation(result);
        return result;
    }

    result = read_file(source_image, &picture);
    if (result != READ_OK){
        print_error_read(result);
        return result;
    }

    rotated_image = rotate_to_angle(&picture, angle);

    result = write_file(source_rotated_image, &rotated_image);
    if (result != WRITE_OK){
        print_error_write(result);
        free(rotated_image.data);
        return result;
    }

    free(rotated_image.data);

    return 0;
}
