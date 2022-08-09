 #!/usr/bin/python2
 import sys, socket

offset = ""
        
try:
   print "\nLocating Offset..."
   s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
   s.connect(("x.x.x.x", 9999))
   s.send(('TRUN /.:/' + offset))
   s.close()

except:            
   print "\nError Connecting to Server"
   sys.exit()
