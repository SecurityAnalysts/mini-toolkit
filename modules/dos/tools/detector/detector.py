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
   # os.system('sh ../blocker/blocker redirect ' + ip)
     o = commands.getoutput("sh ../blocker/blocker redirect " + ip)
     r = commands.getoutput("sh ../blocker/timer.sh ip " + ip)
   # subprocess.call(["iptables", "-I", "INPUT", "-s", ip, "-j", "DROP"])
   # subprocess.call(["sh", "../blocker/blocker", "redirect", ip, "&&", "echo", ip])
   # subprocess.call(["iptables", "-D", "INPUT", "-s", "192.168.1.1", "-j", "DROP"])
   # subprocess.call(["iptables", "-D", "OUTPUT", "-s", "192.168.1.1", "-j", "DROP"])
