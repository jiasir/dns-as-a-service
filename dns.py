#!/usr/bin/env python
# DNS management for OpenStack
# Author: jiasir (Taio Jia) <jiasir@icloud.com>
# Source Code: https://github.com/nofdev/dns-as-a-service



import sys
import os
import logging
import re
import string



# create logger
logger = logging.getLogger('dns')
logging.basicConfig(filename='dns.log', level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s' )


# get record from openstack api
def getRecord():
	return ['1.1.1.1', 'test.test.com']

record = getRecord()
ip = record[0]
domain = record[1]




def write_host(ip, domain):
	#Append to the hosts file.
	with open('hosts', 'a') as hosts:
		hosts.write(ip + ' ' + domain + '\n')


		
def replace_domain(ip, domain):
	with open('hosts', 'r') as hosts:
		for line in hosts:
			line = line.split()
			if line[1] in domain:
				os.system('sed -i "s/{0}/{1}/g" hosts'.format('line', 'ip' + ' ' + 'domain'))
			else:
				pass

				
replace_domain('2.2.2.2', 'www.123.com')




		
