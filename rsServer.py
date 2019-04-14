import socket
import sys
import os

def main():

    HOST = "127.0.0.1"
    PORT = 5007

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)

    print("[+] waiting pcap file ...\n")

    while True:
        conn, addr = s.accept()
        print("[+] Receiving file from ", addr)

        fname = "remote_sniffed"+str(addr)+".pcap"
        # get file name to download
        f = open(fname, "wb")
        # f = open("test.zip", "wb")

        while True:
            # get file bytes
            data = conn.recv(4096)
            if not data:
                break
            # write bytes on file
            f.write(data)
        f.close()
        print("[+] pcap file downloaded!")

        sys.exit(0)

if __name__ == '__main__':
    print"""
                                  _                   _  __  __
                                 | |                 (_)/ _|/ _|
         _ __ ___ _ __ ___   ___ | |_ ___   ___ _ __  _| |_| |_ ___ _ __
        | '__/ _ \ '_ ` _ \ / _ \| __/ _ \ / __| '_ \| |  _|  _/ _ \ '__|
        | | |  __/ | | | | | (_) | ||  __/ \__ \ | | | | | | ||  __/ |
        |_|  \___|_| |_| |_|\___/ \__\___| |___/_| |_|_|_| |_| \___|_|
                        client-server mitm tool
    """
    # while 1:
    main()
