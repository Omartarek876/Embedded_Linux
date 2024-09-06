# import socket

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4, TCP
# ip = socket.gethostbyname(socket.gethostname())
# print("Your IP is: " + ip)
# print("===============================")
# s.bind((ip, 5000))
# s.listen(5)

# while True:
#     client, address = s.accept()  # Waiting
#     rodata = client.recv(1024)
#     print(f"{address} is sending to you this message: {rodata.decode('UTF-8')}")
#     print("===============================")
#     msg = str(input("Please enter the message that you want to send: "))
#     msg_encoded = msg.encode('UTF-8')
#     client.send(msg_encoded)
#     client.close()




import socket
import threading

def handle_client(client_socket, address):
    print(f"Connection from {address} has been established.")
    while True:
        try:
            rodata = client_socket.recv(1024)
            if not rodata:
                break
            print(f"{address} is sending to you this message: {rodata.decode('UTF-8')}")
            msg = input("Please enter the message that you want to send: ")
            msg_encoded = msg.encode('UTF-8')
            client_socket.send(msg_encoded)
        except ConnectionResetError:
            break
    client_socket.close()
    print(f"Connection with {address} closed.")

def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = socket.gethostbyname(socket.gethostname())
    print("Your IP is: " + ip)
    print("===============================")
    s.bind((ip, 5000))
    s.listen(5)
    
    while True:
        client_socket, address = s.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
        client_thread.start()

if __name__ == "__main__":
    start_server()
