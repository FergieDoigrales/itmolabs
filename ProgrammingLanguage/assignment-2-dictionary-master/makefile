ASM=nasm
ASM_KEYS=-f elf64 -o
LD=ld

.PHONY: clean test

main: main.o dict.o lib.o
	$(LD) -o main main.o dict.o lib.o
	
%.o:%.asm
	$(ASM) $(ASM_KEYS) $@ $<

main.o: *.inc
	$(ASM) $(ASM_KEYS) main.o main.asm

dict.o: lib.inc
	$(ASM) $(ASM_KEYS) dict.o dict.asm


clean:
	rm -rf *.o main

test:
	python3 test.py
	