import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('localhost',8000))
a=input("Admin :)  Please Enter the word: ")
s.send(a.encode('utf-8'))
print("Data sent")
