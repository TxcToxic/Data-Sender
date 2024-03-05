import socket

def start_client(server_host, server_port, file_path):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))

    # Send File
    with open(file_path, "rb") as file_to_send:
        data = file_to_send.read(1024)
        while data:
            client_socket.send(data)
            data = file_to_send.read(1024)

    client_socket.close()

if __name__ == "__main__":
    server_host = "127.0.0.1"
    server_port = 6767 
    file_path = "send.txt"

    start_client(server_host, server_port, file_path)
