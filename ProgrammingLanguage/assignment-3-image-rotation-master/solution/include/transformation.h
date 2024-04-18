#include "image_struct.h"

#ifndef TRANSFORMATION_H
#define TRANSFORMATION_H

/* создаёт копию изображения, которая повёрнута на 90 градусов */
void rotate( struct image* picture );

struct image rotate_to_angle(struct image* picture, int angle);

#endif
