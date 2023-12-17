import socket

def receive_file(conn, file_path):
    # Receive the file size from the server
    file_size_bytes = conn.recv(4)
    file_size = int.from_bytes(file_size_bytes, byteorder='big')

    # Receive the file data from the server
    file_data = conn.recv(file_size)

    # Save the received file data to a file
    with open(file_path, "wb") as file:
        file.write(file_data)

    print(f"File received and saved as '{file_path}'.")

def main():
    # Set up the client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("10.0.0.220", 8080))

    try:
        # Specify the path where the received PNG file will be saved
        received_file_path = "received_file.png"

        # Receive the PNG file from the server
        receive_file(client_socket, received_file_path)

    except KeyboardInterrupt:
        pass

    finally:
        # Close the socket
        client_socket.close()

if __name__ == "__main__":
    main()
