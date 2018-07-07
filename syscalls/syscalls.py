#! /usr/bin/python

import argparse

parser = argparse.ArgumentParser(description="syscalls.py is a simple python script which list down system_calls in x86, x86_64 assembly. Default value is 32. So if you didn't parse any options it shows you only system_calls related to 32 bit architecture.")
parser.add_argument("-a", type=int, help='Architecture. Eg : 86 ')

args = parser.parse_args()

ncolr = '\x1b[0m'

if args.a == 32 or args.a == 64:

	colr = '\x1b[1;32m'

	path = "/usr/include/asm/unistd_" + str(args.a) + ".h"

	with open( path ,'r') as file:
		for line in file:
			if(line.startswith('#define __NR_')):
				syscall,id = line.split("__NR_")[1].split(" ")
				print( colr + '{0: <24}'.format(syscall) + ncolr + ' : ' + id.rstrip())
elif args.a == None:

	colr = '\x1b[1;32m'

	path = "/usr/include/asm/unistd_32.h"

	with open( path ,'r') as file:
		for line in file:
			if(line.startswith('#define __NR_')):
				syscall,id = line.split("__NR_")[1].split(" ")
				print( colr + '{0: <24}'.format(syscall) + ncolr + ' : ' + id.rstrip())
else:
	wcolr = '\x1b[1;31m'
	print ( wcolr + "Invalid architecture.please use either 32 or 64. \nTry './syscalls.py --help' for more information." + ncolr )
