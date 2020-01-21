import subprocess
import numpy as np
import commands

port = 80
rep = 14
cIP = 3

res = subprocess.check_output(["netstat", "-antu"])
res = res.split('\n')[2:] 

ips = []

for line in res:
    line = line.split(' ')
    i = 0
    for c in line:
        if (c != ''):
            if i == cIP:
                ips.append(c)
            else:
                i += 1

ips = np.array([ip[:-(1 + len(str(port)))] for ip in ips
    if str.endswith(ip, ":" + str(port))])

ipsU, cu = np.unique(ips, return_counts=True)

ipsA = ipsU[cu > rep]

for ip in ipsA:
     o = commands.getoutput("sh ../blocker/blocker redir2attackers " + ip)
                          #   iptables -t nat -I PREROUTING -s 192.168.1.1 -p tcp --dport 80 -j REDIRECT --to-destination 192.168.1.1
                          #   iptables -t nat -I OUTPUT -s 192.168.1.1 -p tcp -o lo --dport 80 -j REDIRECT --to-destination 192.168.1.1


