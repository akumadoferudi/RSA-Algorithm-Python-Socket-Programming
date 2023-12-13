# first of all import the socket library 
import socket
import pickle
import sys
from generate_key import *   
 
# next create a socket object 
# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the local machine name and a port
host = socket.gethostname()
port = 12345

# Bind to the port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(5)

print('Server listening....')

# Establish connection with a client
client_socket, addr = server_socket.accept()
print('Got connection from', addr)

# Generate RSA keys
public_key, private_key = generate_keypair()

# Send public key to client
client_socket.send(pickle.dumps(public_key))

while True:
    

    # Receive encrypted message from client
    encrypted_message = client_socket.recv(4096)
    encrypted_message = pickle.loads(encrypted_message)

    # Decrypt the received message
    decrypted_message = decrypt(private_key, encrypted_message)
    print('Received encrypted message:', encrypted_message)
    print('Decrypted message:', decrypted_message)
    print("\n")
    
    if decrypted_message == 'exit01':
      print('ok, bye!')
      client_socket.close()
      break

sys.exit(0)