import socket

def start_server(host='localhost', port=5003):
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        server_socket.bind((host, port))
        print(f"Server started at {host}:{port}")
        
        server_socket.listen(5)
        print("Waiting for a connection...")
        
        while True:
            # Accept a connection from a client
            client_socket, client_address = server_socket.accept()
            print(f"Connected by {client_address}")
            
            # Receive and respond to data
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                print(f"Received: {data.decode()}")
                client_socket.sendall(b"Message received")
            
            # Close the client connection
            client_socket.close()
            print(f"Connection with {client_address} closed")
    
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server_socket.close()
        print("Server shut down")

if __name__ == "__main__":
    start_server()
