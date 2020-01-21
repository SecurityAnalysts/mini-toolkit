#!/usr/bin/env python

import time
import socket
import commands

def config():
	l = ''
	hostname = '0.0.0.0'
        port = 8089
	return (hostname, port, l)

def logs(client, data):
	spc = '-------------------------------------------------------'
	o = open('ddos.log', 'a')
	o.write('Time: %s\nIP: %s\nPort: %d\nData: %s\n%s\n\n'%(time.ctime(), client[0], client[1], data, spc))
        #r = commands.getoutput('echo "IP: %s"'% client[0]) # Bloqueo de IPTABLES
        print 'Time: %s\nIP: %s\nPort: %d\nData: %s\n%s\n\n'%(time.ctime(), client[0], client[1], data, spc)
        #print r
	o.close()

def main(hostname, port, l):
	print "[*] Server Started"
	sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sockt.bind((hostname, port))
	sockt.listen(100)
	while True:
		(insock, address) = sockt.accept()
		print ''
		try:
			insock.send('%s\n'%(l))
			data = insock.recv(1024)
			insock.close()
		except socket.error, e:
			logs(address)
		else:
			logs(address, data)
        
if __name__=='__main__':
	try:
		stuff = config()
		main(stuff[0], stuff[1], stuff[2])
	except KeyboardInterrupt:
		print 'Bye!'
		exit(0)
	except BaseException, e:
		print 'Error: %s' % (e)
exit(1)

