%include "lib.inc"

section .text

global find_word

find_word:
	push rbx
	push r12
	xor rax, rax
	.loop:
		test rsi, rsi
		jz .end
		mov rbx, rsi
		add rsi, 8
		mov r12, rdi
		call string_equals
		mov rdi, r12
		test rax, rax
		jnz .is_find
		mov rsi, [rbx]
		jmp .loop
	.is_end:
		xor rax, rax
		jmp .end
	.is_find:
		mov rax, rbx
	.end:
		pop r12
		pop rbx
		ret
		