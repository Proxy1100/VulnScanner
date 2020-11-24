#!/usr/bin/python



# Socket lib is mainly used for  returing  waether the ports are open or closed.
import socket

# os lib  have some function to work with os and mainly it is used for  handling files like read,write,append, open,close files
import os
# sys lib  used for accepting input and output while in runtime error , mainly it uses for passing argument using python from commad line
import sys 



def  returnbanner(ip,port):
		try:
			socket.setdefaulttimeout(2)
			s = socket.socket()
			s.connect((ip,port))
			banner =  s.recv(1024)
			return  banner
		except:
			return


def checkvuln(banner, filename):
		f = open(filename, "r")
		for line in f.readlines():
			 if line.strip('/n') in banner:
				 print "[+] Server is Vulnerable:" + banner.strip('/n')


#definig main function
def main():
	 if len(sys.argv)==2:
		filename=sys.argv[1]
		if not os.path.isfile(filename):
			print "[-] File Doesn't Exits"
			exit(0)
		if not os.access(filename,os.R_OK):
			print "[-] Access Denied"
			exit(0)
	 else:
		print 'Usage:'+ str(sys.argv[0]) + " <Vuln filename>"
		exit(0)
	 portlist =[21,22,23,25,53,443,110,135,139,1433,1434]
	 for x in range(120,140):
		    ip="192.168.222."+ str(x)
		    print 'checking for Vuln in =>' + ip
		    for port in portlist:
			        banner = returnbanner(ip,port)
				if banner:
						print "[*]"+ ip + "/" + str(port) + ":" + banner
						checkvuln(banner,filename)

main()













