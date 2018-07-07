## Linux-Assembly-x86_64

To find out your **processor type** , **the way of the store data in memory** (this depends on the structure of the processor,there're two way of storing data in memory,*Big Endian* and *Little Endian*) and etc. Use `lscpu` command.

### Installing nasm 

`apt install nasm`

### Creating executable from nasm script

`nasm -f elf64 -o <fileName>.o <fileName>.asm` to create the object file.

`ld -o <fileName> <fileName>.o` to create the executable file.

`./<fileName>`



#### syscalls repo ###

This contains a simple python3 script ([syscalls.py](https://github.com/ChathuraDR/Linux-Assembly-x86_64/blob/master/syscalls/syscalls.py)) which list down system_calls in x86, x86_64 assembly. Default value is 32. So if you didn't parse any options it shows you only system_calls related to 32 bit architecture.

### Useful links 
[system_calls related to x86 architecture](http://syscalls.kernelgrok.com/)

[system_calls related to x86_64 architecture](http://blog.rchapman.org/posts/Linux_System_Call_Table_for_x86_64/)


