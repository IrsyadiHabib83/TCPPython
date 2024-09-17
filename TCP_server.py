import socket

def tcp_server():
    host = '127.0.0.1'  # Alamat lokal atau ganti ke publik jika menggunakan ip publik
    port = 65432         # Port server (sesuaikan dengan kebutuhan)

    # Membuat socket TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))  # Binding alamat dan port
        s.listen()            # Server mulai mendengarkan permintaan dari client

        print(f"Server listening on {host}:{port}...")

        # Menerima koneksi dari client
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")

            while True:
                # Menerima data dari client
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Received from client: {data.decode('utf-8')}")
                
                # Mengirim balik pesan ke client
                conn.sendall(data)

if __name__ == "__main__":
    tcp_server()
