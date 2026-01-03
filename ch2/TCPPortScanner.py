import optparse
from socket import *

# ATTEMPTING CONNECTION FOR PROVIDED HOST AND PORT
def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM) # SOCK_STREAM for TCP, SOCK_DGRAM for UDP
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send(b"C3RT1F13D_SKR1PTK1DD13")

        results = connSkt.recv(100)
        print(f"[+]{tgtPort}/tcp open")
        print(f"[+] {str(results)}")
        connSkt.close()
    except:
        print(f"[-]{tgtPort}/tcp closed")

# RESOLVING HOSTNAME AND ENUMERATING THROUGH EACH PORT FROM PROVIDED PORT LIST
def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print(f"[-] Cannot resolve {tgtHost}: Unknown host")
        return
    try:
        tgtName = gethostbyaddr(tgtIP)
        print(f"\n[+] Scan Results for: {tgtName[0]}")
    except:
        print(f"\n[+] Scan Results for: {tgtIP}")
    setdefaulttimeout(1)

    for tgtPort in tgtPorts:
        print(f"Scanning port {tgtPort}")
        connScan(tgtHost, int(tgtPort))

def main():
    # PARSING OUR TARGET HOSTNAME AND PORT TO SCAN
    parser = optparse.OptionParser('usage%prog -H <target host> -p <target port>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='string', help='specify target port[s] separated by comma')
    (options, args) = parser.parse_args()

    tgtHost = options.tgtHost
    tgtPorts = [p.strip() for p in options.tgtPort.split(',') if p.strip()]
    if (tgtHost == None) or (tgtPorts[0] == None):
        print(parser.usage)
        exit(0)
    portScan(tgtHost, tgtPorts)

if __name__ == '__main__':
    main()