import socket

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Running at: {host}:{port}")

    while True:  # Keep Alive
        client_socket, client_address = server_socket.accept()
        print(f"Client [{client_address}] connected")

        # Receive File
        received_file = open("recv_file.txt", "wb")  # currently not dynamic
        data = client_socket.recv(1024)
        while data:
            received_file.write(data)
            data = client_socket.recv(1024)

        received_file.close()
        client_socket.close()  # to keep the one client slot free

if __name__ == "__main__":
    server_host = "127.0.0.1"
    server_port = 6767

    start_server(server_host, server_port)
