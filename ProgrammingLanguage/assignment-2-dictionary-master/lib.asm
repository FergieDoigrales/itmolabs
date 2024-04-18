%define NEXTLINE_S 0xA
%define TAB_S 0x9
%define EXIT_SC 60
%define WRITE_SC 1
%define STDOUT 1
%define SPACE_S 0x20

global exit
global string_length
global print_string
global print_char
global print_newline
global print_uint
global print_int
global string_equals
global read_char
global read_word
global parse_uint
global parse_int
global string_copy

section .text
 
 
; Принимает код возврата и завершает текущий процесс
exit: 
    mov rax, EXIT_SC
    syscall

; Принимает указатель на нуль-терминированную строку, возвращает её длину
string_length:
    xor rax, rax
.pointer: 
    cmp byte [rdi], 0
    je .end
    inc rax
    inc rdi
    jmp .pointer
.end:
    ret

; Принимает указатель на нуль-терминированную строку, выводит её в stdout
print_string:
    ;mov rsi, rdi
    push rdi
    call string_length
    pop rsi
    mov rdx, rax
    mov rax, WRITE_SC
    mov rdi, STDOUT
    syscall
    ret

; Переводит строку (выводит символ с кодом 0xA)
print_newline:
    mov rdi, NEXTLINE_S

; Принимает код символа и выводит его в stdout
print_char:
    push rdi
    mov rdi, STDOUT
    mov rax, WRITE_SC
    mov rdx, 1
    mov rsi, rsp
    syscall 
    pop rdi 
    ret

; Выводит беззнаковое 8-байтовое число в десятичном формате 
; Совет: выделите место в стеке и храните там результаты деления
; Не забудьте перевести цифры в их ASCII коды.
    ; Выводит знаковое 8-байтовое число в десятичном формате 
print_int:
  test rdi, rdi
  jge print_uint
  neg rdi
  push rdi
  mov rdi, '-'
  call print_char
  pop rdi

print_uint:
    mov r10, rsp
    push 0 
    mov rax, rdi        
    mov rdi, 10     ; Для реализации цикла деления числа на 10
    xor rdx, rdx    ; 
    xor rcx, rcx
    
.loop:
    div rdi   ; rax/rdi, результат в rax, остаток в rdx
    add rdx, "0"
    dec rsp               
    mov byte[rsp], dl     
    xor rdx, rdx
    inc rcx
    test rax, rax
    jne .loop
.print:
    mov rdi, rsp
    push r10
    call print_string
    pop rsp
    ret


; Принимает два указателя на нуль-терминированные строки, возвращает 1 если они равны, 0 иначе
;Принимает два указателя на нуль-терминированные строки, ;возвращает 1 если они равны, 0 иначе
string_equals:
.loop:
    mov dl, byte[rdi]
    cmp dl, byte[rsi]
    jne .notequals1
    inc rsi
    inc rdi
    test dl, dl
    jz .equals1
    jmp .loop
.notequals1:
    xor rax, rax
    ret
.equals1:
    mov rax, 1
    ret



; Читает один символ из stdin и возвращает его. Возвращает 0 если достигнут конец потока
read_char:
    push 0 
    xor rax, rax
    xor rdi, rdi        
    lea rsi, [rsp]
    mov rdx, 1
    syscall  
    pop rax
    ret


; Принимает: адрес начала буфера, размер буфера
; Читает в буфер слово из stdin, пропуская пробельные символы в начале, .
; Show 20 lines  Show all unchanged lines  Show 20 lines
; Эта функция должна дописывать к слову нуль-терминатор

read_word:
 
    xor rax, rax

    push r15
    push r14
    push r13

    mov r15, rdi ; pointer
    mov r14, rsi ; размер
    xor r13, r13 ; counter
    
    .loop:
        call read_char
                      
        cmp al, NEXTLINE_S
        jz .symb
        cmp al, TAB_S
        jz .symb
        cmp al, ` `
        jz .symb

        cmp r13, r14
        jge .clear

        test rax, rax  
        jz .end
        
        mov [r15 + r13], al
        inc r13

        jmp .loop

    .symb:
        test r13, r13
        jz .loop
        jnz .end

    .clear:
        xor rax, rax
        jmp .return1

    .end:
        mov byte[r15 + r13], 0
        mov rax, r15
        mov rdx, r13
        jmp .return1

    .return1:
        pop r13
        pop r14
        pop r15
        ret


; Принимает указатель на строку, пытается
; прочитать из её начала беззнаковое число.
; rdx = 0 если число прочитать не удалось
parse_uint:
    xor rax, rax

    xor rcx, rcx
    xor rdx, rdx

    .loop:
        mov al, [rdi + rcx]
        test al, al
        jz  .end
        sub al, '0'     
        js  .end
        cmp al, 9
        ja  .end
        inc rcx
        imul rdx, 10
        add dl, al
        jmp .loop
    .end:
        mov rax, rdx
        mov rdx, rcx
        ret

; Принимает указатель на строку, пытается
; прочитать из её начала знаковое число.
; Если есть знак, пробелы между ним и числом не разрешены.
; Возвращает в rax: число, rdx : его длину в символах (включая знак, если он был) 
; Возвращает в rax: число, rdx : его длину в символах (включая знак, если он был)
; rdx = 0 если число прочитать не удалось
parse_int:
        cmp     byte [rdi], '-'
        je      .negative
        cmp     byte [rdi], '+'
        je      .positive
        jmp     parse_uint
.negative:
        inc     rdi
        call    parse_uint
        inc     rdx
        neg     rax
        ret
.positive:
        inc     rdi
        call    parse_uint
        inc     rdx
        ret


; Принимает указатель на строку, указатель на буфер и длину буфера
; Копирует строку в буфер
; Возвращает длину строки если она умещается в буфер, иначе 0
string_copy:
    xor rax, rax
.loop:
    cmp rax, rdx
    je .err
    mov cl, byte[rdi + rax]
    mov byte[rsi + rax], cl
    inc rax
    test cl, cl
    je .end
    jmp .loop
.err:  
    xor rax, rax
.end:
    ret