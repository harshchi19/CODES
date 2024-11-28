import socket

def start_udp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    message = "Hello from Gaurav UDP client"
    client_socket.sendto(message.encode(), ('localhost', 8080))

    data, addr = client_socket.recvfrom(1024)
    print("Received from server: ", data.decode())

    client_socket.close()

if __name__ == "__main__":
    start_udp_client()