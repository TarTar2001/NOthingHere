import socket

ESP32_IP = '192.168.40.73'
ESP32_PORT = 1234

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the ESP32
s.connect((ESP32_IP, ESP32_PORT))

# Send data to ESP32
s.sendall(b'Hello, ESP32!')

# Receive data from ESP32
data = s.recv(1024)
print('Received:', data.decode())

# Close the connection
s.close()
