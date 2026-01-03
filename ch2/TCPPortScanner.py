import optparse
from socket import *

# PARSING OUR TARGET HOSTNAME AND PORT TO SCAN
parser = optparse.OptionParser('usage %prog -H <target host> -p <target port>')
parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
parser.add_option('-p', dest='tgtPort', type='int', help='specify target port')
(options, args) = parser.parse_args()

tgtHost = options.tgtHost
tgtPort = options.tgtPort
if (tgtHost == None) or (tgtPort == None):
    print(parser.usage)
    exit(0)

# ENUMERATING THROUGH EACH PORT AND ATTEMPTING CONNECTION
def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM) # SOCK_STREAM for TCP, SOCK_DGRAM for UDP
        connSkt.connect((tgtHost, tgtPort))
        print(f"[+]{tgtPort}/tcp open")
        connSkt.close()
    except:
        print(f"[-]{tgtPort}/tcp closed")

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print(f"[-] Cannot resolve {tgtHost}: Unknown host")
        return
    try:
        tgtName = gethostbyaddr(tgtIP)
        print(f"\n[+] Scan Results for: {tgtName[0]}")
        return
    except:
        print(f"\n[+] Scan Results for: {tgtIP}")
    setdefaulttimeout(1)

    for tgtPort in tgtPorts:
        print(f"Scanning port {tgtPort}")
        connScan(tgtHost, int(tgtPort)
                 )
