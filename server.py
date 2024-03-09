import socket
import os

recv_path = os.path.curdir

class recv_folder:
    def creat(name: str = "received") -> bool:
        desktop_path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        if os.path.exists(os.path.join(desktop_path, name)):
           return False
        try:
            os.mkdir(os.path.join(desktop_path, name))
            
            recv_path = os.path.join(desktop_path, name)
            
            with open(os.path.join(desktop_path, name, "readme.txt"), "w") as rmtxt:
                rmtxt.write("!> PLEASE DO NOT REMOVE THIS DIRECTORY <!\n")
                rmtxt.write("this directory was created by data_socket\n\n")
                rmtxt.write("!> You have to create 2 Firewall rules\n")
                rmtxt.write("press win + r then type \"wf.msc\"\n")
                rmtxt.write("now create an in- & outbound rule and allow tcp port 6767")
                rmtxt.close()
            
            return True
        except:
            return False

    def check(name: str = "received") -> bool:
        desktop_path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop', name)
        if os.path.exists(desktop_path):
            recv_path = desktop_path
            return True
        return False

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Running at: {host}:{port}")

    while True:  # Keep Alive
        client_socket, client_address = server_socket.accept()
        print(f"Client [{client_address}] connected")

        # Receive File
        received_file = open(recv_path + "recv_file.txt", "wb")  # currently not dynamic
        data = client_socket.recv(1024)
        while data:
            received_file.write(data)
            data = client_socket.recv(1024)

        received_file.close()
        client_socket.close()  # to keep the one client slot free

if __name__ == "__main__":
    server_host = "127.0.0.1"
    server_port = 6767

    if not recv_folder.check():                                          # Not Important but easier to find 
        # print("Desktop Folder was not found, saving to current dir...")
        recv_folder.creat()
        
    start_server(server_host, server_port)
