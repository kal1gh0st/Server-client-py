# Srver-client-py
You don't say what the actual problem is, or show any errors, but here are some things to check.

Firstly, does the socket actually exist?
Does your client python process have permission to access the socket file?
Is there a server process running that is listening for incoming connections on that socket?
Note that you need a client and a server for communication to take place. The server must already be running before the client can connect. The server creates the socket which must not already exist.

server.py

Run this server, then (in another terminal) run your client code:

client.py
