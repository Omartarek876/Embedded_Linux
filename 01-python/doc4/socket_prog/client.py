# import socket

# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# ip = socket.gethostbyname(socket.gethostname())
# print("Your IP is: " + ip)
# client.connect((ip, 5000))
# print("===============================")

# # while True:
# msg = str(input("Please enter the message that you want to send: "))
# msg_encoded = msg.encode('UTF-8')
# client.send(msg_encoded)

# print("===============================")
# rodata = client.recv(1024)
# print(f"{ip} is sending to you this message: {rodata.decode('UTF-8')}")

# client.close()

import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            rodata = client_socket.recv(1024)
            if not rodata:
                break
            print(f"\nServer is sending this message: {rodata.decode('UTF-8')}")
        except ConnectionResetError:
            break
    client_socket.close()

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = socket.gethostbyname(socket.gethostname())
    print("Your IP is: " + ip)
    client_socket.connect((ip, 5000))
    print("===============================")
    
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()
    # print(f"here : {receive_messages} ") 
    while True: 
            msg = input("Please enter the message that you want to send: ")
            msg_encoded = msg.encode('UTF-8')
            client_socket.send(msg_encoded)

if __name__ == "__main__":
    start_client()
