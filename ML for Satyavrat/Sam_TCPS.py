import socket

def start_tcp_server():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        server_socket.bind(('localhost', 8080))
        
        server_socket.listen(1)
        print("TCP Server is waiting for a connection...")

        conn, addr = server_socket.accept()
        print(f"Connection established with {addr}")

        data = conn.recv(1024)
        print("Received from client: ", data.decode())

        response = "Hello this is Gaurav"
        conn.sendall(response.encode())

        conn.close()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_tcp_server()