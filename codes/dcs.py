import socket
 cmd = socket.socket()
 cmd.connect(("127.0.0.1",7778))
 str_cache=cmd.recv(1024)
 print(str_cache.decode(encoding="utf-16"))
 cmd.close()
