#include <stdint.h>
#include <stdio.h>

#include "image_struct.h"

#ifndef FROM_TO_H
#define FROM_TO_H

#pragma pack(push, 1)
struct bmp_header
{
    uint16_t bfType;
    uint32_t bfileSize;
    uint32_t bfReserved;
    uint32_t bOffBits;
    uint32_t biSize;
    uint32_t biWidth;
    uint32_t biHeight;
    uint16_t biPlanes;
    uint16_t biBitCount;
    uint32_t biCompression;
    uint32_t biSizeImage;
    uint32_t biXPelsPerMeter;
    uint32_t biYPelsPerMeter;
    uint32_t biClrUsed;
    uint32_t biClrImportant;
};
#pragma pack(pop)

/*  deserializer   */
enum read_status  {
    READ_OK = 0,
    READ_INVALID_BITS,
    READ_INVALID_HEADER,
    READ_CANNOT_READING,
    READ_NO_NAME
};

enum read_status from_bmp( FILE* in, struct image* img );

/*  serializer   */
enum  write_status  {
    WRITE_OK = 0,
    WRITE_CANNOT_WRITING
};

enum write_status to_bmp( FILE* out, struct image const* img );

enum read_status read_file(char* source_image, struct image* picture);

void print_error_read(enum read_status res);

enum write_status write_file(char* source_rotated_image, struct image* rotated_image);

void print_error_write(enum write_status res);



#endif
