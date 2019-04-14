from scapy.all import sniff, wrpcap
import sys, socket, os


TCP_IP = '127.0.0.1'
TCP_PORT = 5007

global pkg_lst
PCAP_FILE = 'testeo.pcap'
pkg_lst = sniff(filter="http")
wrpcap(PCAP_FILE, pkg_lst)

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect((TCP_IP, TCP_PORT))
with open(PCAP_FILE, "rb") as f:
    data = f.read()
    conn.sendall(data)
    # close connection
    conn.close()
    sys.exit(0)
    # break
os.remove(PCAP_FILE)
