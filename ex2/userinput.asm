section .data
	text db "What is your name? "
	op db "Hello, "

section .bss
	name resb 16 ; reserve 16 bytes

section .text
	global _start

_start:

	call _getName
	call _printName
	mov rax,60
	mov rdi,0
	syscall

_getName:
	mov rax,1
	mov rdi,1
	mov rsi,text
	mov rdx,19
	syscall
	
	mov rax,0
	mov rdi,0
	mov rsi,name
	mov rdx,16
	syscall
	ret

_printName:
	mov rax,1
	mov rdi,1
	mov rsi,op
	mov rdx,9
	syscall

	mov rax,1
	mov rdi,1
	mov rsi,name
	mov rdx,16
	syscall
	ret

