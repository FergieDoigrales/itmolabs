%include "lib.inc"
%include "dict.inc"
%include "words.inc"

%define BUF_LENGTH 256
%define NEXT_ELEM 8
%define PRINT 1
%define STDERR 2

section .rodata
err_long_key: db "too long key", 0
err_not_found: db "not found key", 0

section .bss
buffer: resb BUF_LENGTH

section .text
global _start

_start:
    mov rdi, buffer
    mov rsi, BUF_LENGTH
    call read_word
    test rax, rax
    jz .too_long_err 
    push rdx 
    mov rdi, rax 
    mov rsi, top
    call find_word
    pop rdx
    test rax, rax
    jz .not_found_err
    add rax, NEXT_ELEM
    add rax, rdx 
    inc rax 
    mov rdi, rax
    call print_string
    .complete:
        xor rdi, rdi
        call exit
    .too_long_err:
        mov rdi, err_long_key
        jmp .error
    .not_found_err
        mov rdi, err_not_found
    .error:
        call print_error
        jmp .complete

print_error:
	push rdi
	call string_length
	pop rsi
	mov rdx, rax
	mov rax, PRINT
	mov rdi, STDERR
	syscall
	ret
