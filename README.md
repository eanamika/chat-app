# TCP Multi-Client Chat Application

## Overview
This project is a simple **multi-client chat application** built using **TCP socket programming in Python**. It allows multiple users to connect to a central server and exchange messages in real time. The system follows a **client–server architecture**, where the server manages connections and broadcasts messages between clients.

The project demonstrates key networking concepts such as **TCP communication, sockets, and multithreading**.

---

## Features
- Multiple clients can connect simultaneously
- Real-time message broadcasting
- Username-based chat identification
- Join and leave notifications
- Concurrent client handling using threads
- Simple command-based communication protocol

---

## Technologies Used
- Python 3
- TCP Socket Programming
- Multithreading
- Client–Server Architecture

---

## Project Structure
```
chat-application/
│
├── server.py    # Server program that manages clients
├── client.py    # Client program used by users
└── README.md
```

---

## Communication Protocol

The application uses a simple text-based protocol:

| Command | Description |
|--------|-------------|
| JOIN username | Client joins the chat |
| MSG message | Send message to other clients |
| QUIT | Leave the chat |

Example:
```
JOIN Anamika
MSG Hello everyone
QUIT
```

---

## How to Run

### 1. Start the Server
Open a terminal and run:

```bash
python server.py
```

Output:
```
[LISTENING] Server is running on 127.0.0.1:5555
```

---

### 2. Start the Client
Open another terminal and run:

```bash
python client.py
```

Enter your username when prompted.

---

### 3. Send Messages
Type your message and press Enter.

Example:
```
> Hello everyone
```

---

### 4. Leave Chat
To exit the chat, type:

```
/quit
```

---

## Example Chat

User 1:
```
Enter your username: Anamika
> Hello
```

User 2:
```
Enter your username: Swarnali
Anamika: Hello
> Hi Anamika
```

---

## Learning Outcomes
- Understanding TCP socket programming
- Implementing client–server communication
- Handling multiple clients using multithreading
- Designing a simple messaging protocol

---

## Limitations
- Works only on local network
- No encryption for messages
- No graphical user interface
- No message storage

---

## Future Improvements
- Add GUI using Tkinter or a web interface
- Implement message encryption
- Add chat rooms
- Store chat history in a database
- Deploy server on the cloud
