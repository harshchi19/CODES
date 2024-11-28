import socket

def start_udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_socket.bind(('localhost', 8080))
    print("UDP Server is listening...")

    while True:
        data, addr = server_socket.recvfrom(1024)
        print(f"Received from {addr}: {data.decode()}")

        response = "Hello from Gaurav UDP server"
        server_socket.sendto(response.encode(), addr)

if __name__ == "__main__":
    start_udp_server()