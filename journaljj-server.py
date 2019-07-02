import socket          
import datetime
import encryption

with open ('key.txt','r') as file:
	key=file.read().strip()


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
sock.bind(("0.0.0.0", 8088))                  
sock.listen(5)                 

encryption=encryption.ENCRYPTION_ECB(key)

while True: 
	conn, addr = sock.accept()
	with conn:
		print('Connected by '+addr[0]+' '+datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
		while True:
			data = conn.recv(1024)
			if not data:
				print("Disconnected...")
				break
			else:
				print (data.decode())
				#print (encryption.decrypt(data.decode().strip()))
				with open ("journal.txt","a") as file:
					file.write('Connected by '+str(addr)+', '+datetime.datetime.now().strftime("%Y-%m-%d %H:%M")+'\n')
					file.write(data.decode())
			

