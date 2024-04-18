#include <stdlib.h>

#include "fromto.h"

static char *ErrorRead[] = {
        "Everything is OK",
        "Empty data",
        "Header is invalid",
        "Rights is not enough",
        "Source is not found"
};


static char *ErrorWrite[] = {
        "Everything is OK",
        "Cannot writing"

};

void print_error_read(enum read_status res){
    printf("%s", ErrorRead[res]);
}

enum read_status read_file(char* source_image, struct image* picture){
    FILE *pict;
    if (source_image) {
        pict = fopen(source_image, "rb");
        if (pict) {
            enum read_status status = from_bmp(pict, picture);
            fclose(pict);
            return status;
        } else {
            return READ_CANNOT_READING;
        }
    } else {
        return READ_NO_NAME;
    }
}

void print_error_write(enum write_status res){
    printf("%s", ErrorWrite[res]);
}

enum write_status write_file(char* source_rotated_image, struct image* rotated_image){
    FILE *pctr;
    if (source_rotated_image) {
        pctr = fopen(source_rotated_image, "wb");
        if (pctr) {
            enum write_status status = to_bmp(pctr, rotated_image);
            fclose(pctr);
            return status;
        }
    }

    return WRITE_CANNOT_WRITING;
}


static uint8_t calculate_padding(uint64_t width) {
    return 4 - width * sizeof(struct pixel) % 4;
}

enum read_status from_bmp(FILE *in, struct image *img) {
    struct bmp_header *header = malloc(sizeof(struct bmp_header));

    if (fread(header, sizeof(struct bmp_header), 1, in) != 1) {
        free(header);
        return READ_INVALID_HEADER;
    };
    img->height = header->biHeight;
    img->width = header->biWidth;
    img->data = malloc(sizeof(struct pixel) * img->height * img->width);
    for (size_t i = 0; i < img->height; i++) {
        if (fread(img->data + i * img->width, sizeof(struct pixel), img->width, in) != img->width) {
            free(img->data);
            return 0;
        }
        fseek(in, calculate_padding(img->width), SEEK_CUR);
    }
    if (!img->data) {
        free(header);
        return READ_INVALID_BITS;
    }
    free(header);

    return READ_OK;
}

enum write_status to_bmp(FILE *out, struct image const* img) {
    struct bmp_header *header = malloc(sizeof(struct bmp_header));
    uint8_t padding = calculate_padding(img->width);

    header->bfType = 0x4D42;
    header->bfileSize = sizeof(struct bmp_header) + sizeof(struct pixel) * (img->width * padding) * img->height;
    header->bfReserved = 1;
    header->bOffBits = sizeof(struct bmp_header);
    header->biSize = 40;
    header->biWidth = img->width;
    header->biHeight = img->height;
    header->biPlanes = 1;
    header->biBitCount = 24;
    header->biCompression = 0;
    header->biSizeImage = (img->width + padding) * img->height;
    header->biXPelsPerMeter = 1;
    header->biYPelsPerMeter = 1;
    header->biClrUsed = 0;
    header->biClrImportant = 0;

    fwrite(header, sizeof(struct bmp_header), 1, out);
    for (size_t i = 0; i < img->height; i++) {
        if (fwrite(img->data + i * img->width, sizeof(struct pixel), img->width, out) != img->width) {
            free(header);
            return WRITE_CANNOT_WRITING;
        };
        fseek(out, padding, SEEK_CUR);
    }
    free(header);
    return WRITE_OK;
}


