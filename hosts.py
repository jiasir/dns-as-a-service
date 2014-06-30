#!/usr/bin/env python3.4

import sys, os

argv = sys.argv

# Some usage information.
def usage():
	print("Usage: %s <211.151.168.182> <www.shangpin.com>" %(os.path.basename(argv[0])))

if not len(argv) == 3:
	usage()
	exit(1)


# Argv 1 as ip, Argv 2 as domain that you want to added.
ip = argv[1]
domain = argv[2]

#Append to the hosts file.
with open('hosts', 'a') as hosts:
	hosts.write(ip + ' ' + domain + '\n')


# Print content of the hosts.
print('Current hosts file contents are:')

with open('hosts', 'r') as hosts:
	for each_line in hosts:
		print(each_line, end='')



		
