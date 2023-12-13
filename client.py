import socket
import pickle
import sys
from generate_key import *

# RSA functions (similar to the previous code)

# Other RSA functions (is_prime, gcd, mod_inverse, generate_keypair, encrypt, decrypt) as shown before

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the server machine name and port
host = socket.gethostname()
port = 12345

# Connect to the server
client_socket.connect((host, port))

# Receive the public key from server
public_key = pickle.loads(client_socket.recv(4096))

while True:
    # Your message to be sent
    # message = "Hello, RSA Encryption!"
    message = input('enter your message: ')

    if message == 'exit01':
        # Close the socket
        print('bye-bye server')
        encrypted_message = encrypt(public_key, message)
        client_socket.send(pickle.dumps(encrypted_message))
        break

    # Encrypt the message using the received public key
    encrypted_message = encrypt(public_key, message)
    print('Original Message:', message)
    print('Encrypted Message:', encrypted_message)
    print("\n")

    # Send the encrypted message to the server
    client_socket.send(pickle.dumps(encrypted_message))

client_socket.close()
sys.exit(0)