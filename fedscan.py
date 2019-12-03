import socket as so
import subprocess as sp
import sys

def Red(skk): print("\033[91m {}\033[00m" .format(skk)) 
def LightPurple(skk): print("\033[94m {}\033[00m" .format(skk)) 

def queryDomain():
    while True:
        ipDom = raw_input("Scan (i)P or (d)omain(i/d)? > ")
        if ipDom == 'd':
            return True
        if ipDom == 'i':
            return False

sp.call('clear', shell=True)

if queryDomain():
    domain = raw_input("Enter domain name > ")
    try:
        ip_scan = so.gethostbyname(domain)
        print("IP of " + domain + " is :")
        LightPurple(ip_scan)
    except:
        print("Unknown hostname " + domain)
        sys.exit()
else:
    ip_scan = raw_input("Enter IP to scan > ")

while True:
    minP = input("Port range from? : ")
    maxP = input("Port range to? : ")
    if minP <= maxP:
        break
    print("Min port must be <= max port")

print ""
print "Executing scan... Please wait"
print ""

for port in range(minP, maxP + 1):
    s = so.socket(so.AF_INET, so.SOCK_STREAM)
    if not s.connect_ex((ip_scan, port)):
        Red("[+] Port {} is open".format(port))
    s.close()