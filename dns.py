#!/usr/bin/env python3.4
# DNS management for ci-aotumation project
# Author: jiasir (Taio Jia) <jiasir@icloud.com>
# Source Code: https://github.com/nofdev/dns-as-a-service



import sys
import os
import logging

# create logger
logger = logging.getLogger('dns')
logging.basicConfig(filename='dns.log', level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s' )

argv = sys.argv

# Some usage information.
def usage():
	print("Usage: {} <211.151.168.182> <www.shangpin.com>".format(os.path.basename(argv[0])))

if not len(argv) == 3:
	usage()
	exit(1)


# Argv 1 as ip, Argv 2 as domain that you want to added.
ip = argv[1]
domain = argv[2]

def writeHost(ip, domain):
	#Append to the hosts file.
	with open('hosts', 'a') as hosts:
		hosts.write(ip + ' ' + domain + '\n')
		
def searchDomain(ip, domain):
	with open('hosts', 'r+') as hosts:
		for x in hosts:
			if x == domain:
				x.replace(ip + domain)



def hosts():
	with open('hosts', 'r') as hosts:
		for each_line in hosts:
			print(each_line, end='')

print('Current hosts file contents are:')
hosts()


		
