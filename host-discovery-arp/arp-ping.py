#/usr/bin/python3
import random
from scapy.all import *
import threading
import time
import ipaddress
import sys

def multiple_hosts():								#Used to scan network based on CIDR notation
	count=0
	checked_host=[]
	while True:
		i=random.randint(0,no_of_hosts-1)
		if i not in checked_host:
			t=threading.Thread(target=arp_ping,args=(dummy[i],))
			t.start()
			count+=1
			checked_host.append(i)
			time.sleep(2)
		if count==no_of_hosts:
			break

def arp_ping(ip):
	active_hosts=[]
	arp=Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=str(ip))
	ans=srp1(arp,timeout=10)
	if ans is None:
		print(str(ip)+' is down!!')
		active_hosts.append(str(ip))
	else:
		print(str(ip) +' is up !!')


conf.verb=0
ip=sys.argv[1]
dummy=[]

if not os.geteuid() == 0:
    print color("[!] ARP-ping must be run as root.")
    sys.exit(-1)
	
if '/' in ip:
	print("Scanning the network.....\n")
	hosts=ipaddress.ip_network(ip)
	for i in hosts:
		dummy.append(i)
	no_of_hosts=len(dummy)
	multiple_hosts()

elif '-h' == ip:
	print('Usage : python3 arp-ping.py 192.168.1.1 \n')
	print('Usage : python3 arp-ping.py 192.168.1.0/24 \n')

else:
	arp_ping(ip)



