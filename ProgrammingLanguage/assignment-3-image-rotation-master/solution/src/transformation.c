#include <stdlib.h>

#include "transformation.h"

struct image rotate_to_angle(struct image* picture, int angle){
    int rotation_counter = angle / 90;

    while (rotation_counter--  > 0) {
        rotate(picture);
    }

    return *picture;
}

void rotate( struct image* picture ) {
    struct image *copied = malloc(sizeof(struct image));
    
    copied->data = malloc(sizeof (struct pixel) * picture->height * picture->width);
    copied->width = picture->height;
    copied->height = picture->width;
    for (size_t i = 0; i < copied->height; i++)
        for (size_t j = 0; j < copied->width; j++)
            copied->data[i * copied->width + j] = picture->data[j * picture->width + picture->width - i - 1];
    free(picture->data);
    picture->data = copied->data;
    picture->width = copied->width;
    picture->height = copied->height;
    free(copied);
}
