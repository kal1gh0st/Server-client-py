import os
import socket

address = '/tmp/socket'
s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
s.bind(address)      # this creates the socket file
s.listen(1)
r, a = s.accept()
r.send('Hello\n')
msg = r.recv(1024)
print msg
r.close()
s.close()
os.unlink(address)    # remove the socket file so that it can be recreated on next run