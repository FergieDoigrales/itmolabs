#include  <stdint.h>

#ifndef IMAGE_STRUCT_H
#define IMAGE_STRUCT_H

struct pixel { uint8_t b, g, r; };

struct image {
  uint64_t width, height;
  struct pixel* data;
};

//int b;
//int* a;
//a = &b;
//b = &(*a);
//a = *(&b);
//print(a); --> адрес
//print(*a); --> значение по адресу a


#endif
