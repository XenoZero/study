import socket
cmd=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
cmd.sendto("MASTER_ARM_SW 1 \n".encode("utf-8"),("127.0.0.1", 7778))
cmd.close()