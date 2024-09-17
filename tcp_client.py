import socket

def tcp_client():
    host = '127.0.0.1'  # Alamat lokal atau ganti ke publik jika menggunakan ip publik
    port = 65432         # Port server (sesuaikan dengan kebutuhan)

    # Membuat socket TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))  # Menghubungkan ke server

        while True:
            # Mengirim pesan ke server
            message = input("Enter message to send: ")
            s.sendall(message.encode('utf-8'))

            # Menerima respon dari server
            data = s.recv(1024)
            print(f"Received from server: {data.decode('utf-8')}")

if __name__ == "__main__":
    tcp_client()
