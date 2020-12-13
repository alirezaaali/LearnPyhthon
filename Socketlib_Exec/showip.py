import socket

hostname = socket.gethostname()
ipadd = socket.gethostbyname(hostname)

print("This is hostname:", hostname)
print("This is Host IP:", ipadd)
