# RSA
import random

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to compute GCD of two numbers
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Extended Euclidean algorithm to find the GCD and coefficients
def extended_euclidean(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_euclidean(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

# Function to compute the modular inverse using extended Euclidean algorithm
def mod_inverse(a, m):
    gcd, x, _ = extended_euclidean(a, m)
    if gcd != 1:
        raise ValueError("Modular inverse doesn't exist.")
    return x % m

# Function to generate public and private keys
def generate_keys(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both p and q must be prime numbers.")
    if p == q:
        raise ValueError("p and q must be different prime numbers.")

    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e such that 1 < e < phi and e is coprime with phi
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    # Calculate d (modular inverse of e modulo phi)
    d = mod_inverse(e, phi)
    return e, d, n

# Function to convert a letter to a number (A = 0, B = 1, ..., Z = 25)
def letter_to_num(letter):
    return ord(letter.upper()) - ord('A')

# Function to convert a number to a letter (0 = A, 1 = B, ..., 25 = Z)
def num_to_letter(num):
    return chr(num + ord('A'))

# RSA encryption
def rsa_encrypt(plaintext, e, n):
    return [pow(letter_to_num(char), e, n) for char in plaintext if char.isalpha()]

# RSA decryption
def rsa_decrypt(ciphertext, d, n):
    return ''.join([num_to_letter(pow(char, d, n)) for char in ciphertext])

# Main function to execute the RSA encryption and decryption process
if __name__ == "__main__":
    try:
        # Get user input for primes p and q
        p = int(input("Enter prime number p: "))
        q = int(input("Enter prime number q: "))

        # Generate RSA keys
        e, d, n = generate_keys(p, q)

        print(f"Public Key (e, n): ({e}, {n})")
        print(f"Private Key (d, n): ({d}, {n})")

        # Get user input for plaintext
        plaintext = input("Enter plaintext to encrypt (only letters): ").strip().upper()

        # Encrypt the plaintext
        ciphertext = rsa_encrypt(plaintext, e, n)
        print(f"Ciphertext: {ciphertext}")

        # Decrypt the ciphertext
        decrypted = rsa_decrypt(ciphertext, d, n)
        print(f"Decrypted: {decrypted}")
    except ValueError as e:
        print(f"Error: {e}")