import socket
import threading

class TCPServer:
  def __init__(self, host='localhost', port=6379):
    self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Allow port reuse
    self.server_socket.bind((host, port))
    self.server_socket.listen(5) # Backlog of 5 connections
    print(f"Server is listening on {host}:{port}")
    
  def run(self):
    try:
      while True:
        connection, address = self.server_socket.accept()
        threading.Thread(target=self.handleClient, args=(connection, address)).start()
    except KeyboardInterrupt:
      print("\nShutting down server...")
    finally:
      self.server_socket.close()
      
  def handleClient(self, connection, address):
    print(f"Connected by {address}")
    
    try:
       while True:
          data = connection.recv(1024).decode().strip()
          if not data:
              break  # Client disconnected
          if data.upper() == "PING":
              connection.send(b"+PONG\r\n")
          else:
              connection.send(b"-ERR Unknown command\r\n")
    except Exception as e:
      connection.send(f"-ERR {str(e)}\r\n".encode())
    finally:
      connection.close()
      print(f"Disconnected: {address}")
    