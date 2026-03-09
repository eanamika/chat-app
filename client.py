import socket
import threading
import sys

def receive_messages(client_socket):
    """Constantly listens for messages from the server."""
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"\n{message}")
                print("> ", end="", flush=True) # Keep the prompt visible
            else:
                break
        except:
            print("[ERROR] Connection lost.")
            break

def start_client():
    # Setup connection
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client.connect(('127.0.0.1', 5555))
    except:
        print("Couldn't connect to server.")
        return

    name = input("Enter your username: ")
    client.send(f"JOIN {name}".encode('utf-8'))

    # Start the background thread for receiving data
    rcv_thread = threading.Thread(target=receive_messages, args=(client,), daemon=True)
    rcv_thread.start()

    print("Type your message and hit Enter. Type '/quit' to leave.")
    
    while True:
        user_input = input("> ")
        
        if user_input.lower() == '/quit':
            client.send("QUIT".encode('utf-8'))
            break
        
        if user_input.strip():
            client.send(f"MSG {user_input}".encode('utf-8'))

    client.close()
    print("Disconnected.")

if __name__ == "__main__":
    start_client()