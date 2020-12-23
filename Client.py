import bluetooth


server = ""
port = 3 


server = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
print("Socket de bluetooth creado")

try:
    server.bind((server,port))
    print("Binding creado")
except: print("binding incompleto")



try:
    
    while True: 
        text =input()
        if text == "quit":
            break
        server.send(text)
         

except KeyboardInterrupt:
    server.close()
    cliente.close()
 