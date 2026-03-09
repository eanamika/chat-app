import socket
import threading

# Config
HOST = '127.0.0.1'
PORT = 5555

clients = {}

def broadcast(message, sender_conn=None):
    """Sends a message to everyone except the person who sent it."""
    for conn in clients:
        if conn != sender_conn:
            try:
                conn.send(message.encode('utf-8'))
            except:
                # If sending fails, the connection is likely dead
                conn.close()
                remove_client(conn)

def remove_client(conn):
    """Clean up when someone leaves."""
    if conn in clients:
        username = clients[conn]
        print(f"[INFO] {username} disconnected.")
        del clients[conn]
        broadcast(f"QUIT {username}")

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    
    try:
        # The first message from the client should be: JOIN <username>
        initial_data = conn.recv(1024).decode('utf-8')
        if initial_data.startswith("JOIN "):
            username = initial_data.split(" ", 1)[1].strip()
            clients[conn] = username
            print(f"[INFO] {username} joined the chat.")
            broadcast(f"JOIN {username} has entered the room!", conn)
        
        # Continuous listening loop
        while True:
            data = conn.recv(1024).decode('utf-8')
            if not data:
                break
            
            if data == "QUIT":
                break
            elif data.startswith("MSG "):
                msg_content = data.split(" ", 1)[1]
                # Format for other clients: Username: message
                broadcast(f"{clients[conn]}: {msg_content}", conn)
                
    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        remove_client(conn)
        conn.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[LISTENING] Server is running on {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        # Start a new thread for every person who joins
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_server()