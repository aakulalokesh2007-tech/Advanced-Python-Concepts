
# 💬 Python GUI Chat Application (Client)

## 📌 Project Overview
A real-time, graphical chat room client built entirely in Python. This application utilizes `socket` programming for network communication, `threading` to handle simultaneous message sending/receiving, and `tkinter` for a clean, user-friendly graphical interface. 

## ✨ Features
* **Custom GUI:** Includes a dedicated login screen for users to enter their display name before entering the chat room.
* **Real-Time Communication:** Uses TCP sockets (`SOCK_STREAM`) to connect to a local server for instantaneous message broadcasting.
* **Non-Blocking Multithreading:** Implements Python's `threading` module to ensure the GUI remains responsive while continuously listening for incoming messages from the server.
* **Zero External Dependencies:** Built using strictly standard Python libraries.

## 🛠️ Built With
* **`tkinter`** - The standard GUI toolkit for Python.
* **`socket`** - For low-level network interface and connecting to the server.
* **`threading`** - To run the message-receiving loop in the background.

## 🚀 Prerequisites
To run this application, you must have:
* Python 3.x installed.
* A running chat server script listening on `127.0.0.1` (localhost) at Port `5000`.

## ⚙️ How to Run
1. Ensure your server-side script is running and listening for connections.
2. Open your terminal or command prompt.
3. Run the client script:
   ```bash
   python client.py
   ```


---
## Output
![Output](lable%20changer.png)
