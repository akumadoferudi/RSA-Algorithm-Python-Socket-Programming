# RSA Algorithm
#
# by: Achmad Ferdiansyah
# github: 

import random
import math
import sys


# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(pow(num, 0.5)) + 1):
        # check if not prime (prime numbers can only divided by 1 and itself)
        if num % i == 0:
            return False
    return True

# Faktor Persekutuan Terbesar (FPB)
# Function to find greatest common divisor (GCD)
# condition 1 < b < a
# GCD my version
def gcd(a, b):
    if b == 0:
        result = a
    else:
        result = gcd(b, a % b)
    return result

# Function to find multiplicative inverse
def multiplicative_inverse(e, phi):
    d = 0
    x1, x2 = 0, 1
    y1, y2 = 1, 0
    temp_phi = phi

    while e > 0:
        # floor division to make value is integer not float
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = y2 - temp1 * y1

        x2 = x1
        x1 = x
        y2 = y1
        y1 = y

    if temp_phi == 1:
        d = y2 + phi

    return d

# Generate large prime numbers 'p' and 'q'
def generate_large_primes():
    primes = [i for i in range(100, 1000) if is_prime(i)]
    # choose random of p, q numbers
    p = random.choice(primes)
    q = random.choice(primes)
    
    # We want p != q
    while p == q:
        q = random.choice(primes)
    return p, q

# Calculate public and private keys
def generate_keypair():
    p, q = generate_large_primes()
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e such that e and phi(n) are coprime
    e = random.randrange(1, phi)
    gcd_value = gcd(e, phi)
    while gcd_value != 1:
        e = random.randrange(1, phi)
        gcd_value = gcd(e, phi)

    # Calculate d, the multiplicative inverse of e mod phi
    d = multiplicative_inverse(e, phi)

    # (e, n) is public key
    public_key = (e, n)
    
    # (d, n) is private key
    private_key = (d, n)
    
    return public_key, private_key

# Encrypt message
def encrypt(public_key, plain_text):
    e, n = public_key
    # translate char to unicode first and calculate
    cipher = [pow(ord(char), e, n) for char in plain_text]
    return cipher

# Decrypt message
def decrypt(private_key, cipher_text):
    d, n = private_key
    # translate claculation to char
    plain = [chr(pow(char, d, n)) for char in cipher_text]
    return ''.join(plain)

# Main
if __name__ == "__main__":
    public_key, private_key = generate_keypair()
    # public_key = (138541, 162121)
    # private_key = (89449, 162121)
    
    # testing public key
    # print(type(public_key))

    # input message
    message = 'halo'
    # message = input('Enter your message: ')
    print("Original message:", message)

    encrypted_message = encrypt(public_key, message)
    print("Encrypted message: " + ''.join(str(el) for el in encrypted_message))
    print("Encrypted message[list version]:", encrypted_message)
    print("Public key:", public_key)

    #  test decrypt
    # private_key = (552223, 383959)
    # decrypted_message = decrypt(private_key, [366123, 3546, 15257, 162612])

    decrypted_message = decrypt(private_key, encrypted_message)
    print("Decrypted message:", decrypted_message)
    print("Private key:", private_key)
