#!/usr/bin/python3
#coded with carinho by Carlos Daniel Giovanella :v

from subprocess import *
import os,sys,time

try:
	if sys.argv[1] == "--ip":
		ipzeira = sys.argv[2]
		os.system('gnome-terminal -e "nmap -T4 -A ' + ipzeira + ' -oN portscan.txt"')
		time.sleep(2)
		if "www." in ipzeira:
			ipsemwww = ipzeira.replace("www.","")
			call("whois " + ipsemwww + " > whois.txt", shell=True)
			time.sleep(5)
			call("nslookup " + ipsemwww + " > nslookup.txt", shell=True)
			time.sleep(1)
			call("dnsenum " + ipsemwww + " > whois.txt", shell=True)
			time.sleep(5)
			call("theharvester -d " + ipzeira + " -b all -f harvester.html -l 1000", shell=True)
		else:
			call("whois " + ipzeira + " > whois.txt", shell=True)
			time.sleep(5)
			call("nslookup " + ipzeira + " > nslookup.txt", shell=True)
			time.sleep(1)
			call("dnsenum " + ipzeira + " > whois.txt", shell=True)
			time.sleep(5)
			call("theharvester -d " + ipzeira + " -b all -f harvester.html -l 1000", shell=True)

		
except IndexError:
	os.system("clear")
	print(''' _ _            _                   _  _      
| | | ___  _ _ | |._ _  _ _  ___  _| |<_> _ _ 
| ' |/ . \| | || || ' || | |<_> |/ . || || '_>
|__/ \___/`___||_||_|_||__/ <___|\___||_||_|  
                                              
 ___            ___  _    _       
/ __> ___  _ _ / __><_> _| |_ ___ 
\__ \/ ._>| | |\__ \| |  | | / ._>
<___/\___.`___|<___/|_|  |_| \___.
                                  ''')
	print ("=======================")
	print ("Tool Creator: Carlos Daniel Giovanella")
	print ("Github: www.github.com/cardangi")
	print ("Facebookerzeira: www.facebook.com/carlosdg1337")
	print ("Currently Age: 16Y ~ Mental age: 2Y :v")
	print ("=======================")
	print ("usage(kali): python3 vouinvadirseusite.py --ip URL")
	print ("URL should be like: www.google.com , no / or http|https")
	print ("")

	
