import bluetooth  #Esta libreria de python funciona solo en linux a veces falla la importacion de la libreria para eso  instale sudo pip3 install pybluez  



host = "";
port=1


server = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
print("Socket de bluetooth creado")

try:
    server.bind((host,port))
    print("Binding creado")
except: print("binding incompleto")

server.listen(1)

cliente, direccion = server.accept()
print("Conectado a:",direccion)
print("Conectado a:",cliente)

data = 'hola mundo'

try:
    while True:
        datos = cliente.recv(1024)
        print (datos)
      
        if datos == b'A':
               cliente.send(data)
               
      
        
        
       
except KeyboardInterrupt:
    server.close()
    cliente.close()
                    
                
