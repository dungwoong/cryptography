import numpy as np
from math import gcd

np.random.seed(42)

def get_invertible_key(n):
    while True:
        key = np.random.randint(0, 26, size=(n, n))
        det = int(round(np.linalg.det(key))) % 26
        if gcd(det, 26) == 1:  # coprime with 26 => invertible mod 26
            return key

def modinv(a, m):
    # returns x such that (a*x) % m == 1
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError("No modular inverse")

def matrix_mod_inv(matrix, modulus):
    det = int(round(np.linalg.det(matrix)))  # determinant
    det_inv = modinv(det, modulus)           # modular inverse of determinant

    # adjugate (classical adjoint) of the matrix
    adj = np.round(det * np.linalg.inv(matrix)).astype(int)  # integer adjugate
    return (det_inv * adj) % modulus

def hill_encrypt(text, key):
    n = key.shape[0]
    # pad text with 'x' if necessary
    if len(text) % n != 0:
        text += 'x' * (n - len(text) % n)

    output = []
    for i in range(0, len(text), n):
        block = np.array([ord(c) - ord('a') for c in text[i:i+n]])
        transformed = key @ block % 26
        output.extend(chr(int(x) + ord('a')) for x in transformed)
    return ''.join(output)

def hill_decrypt(ciphertext, key):
    n = key.shape[0]
    key_inv = matrix_mod_inv(key, 26)

    output = []
    for i in range(0, len(ciphertext), n):
        block = np.array([ord(c) - ord('a') for c in ciphertext[i:i+n]])
        transformed = key_inv @ block % 26
        output.extend(chr(int(x) + ord('a')) for x in transformed)
    return ''.join(output)

key = get_invertible_key(3)
ciphertext = hill_encrypt("attackatdawnyeahelloe", key)
print("Key:\n", key)
print("Ciphertext:", ciphertext)
plain = hill_decrypt(ciphertext, key)
print("Plain:", plain)