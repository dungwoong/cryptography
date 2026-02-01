"""
Key space size
- How large your possible keys can be
- e.g. for caesar cipher, you only have 26 possible keys

For demonstration, let's say that we KNOW the correct output must contain the string "secret"
"""
from toy import caesar

def crack_caesar(text):
    for i in range(26):
        if 'secret' in caesar(text, i):
            return caesar(text, i)
    return None

"""
Kasiski examination for breaking Vigenere
- look for repeating strings in your ciphertext, this can correspond to if you repeatedly encode a word e.g. "the" with the same part of the cipher(cipher is short)
- look at distances between the strings, guess common factors as the key length
- then, create columns in your text, and rotate each column using caesar decryption

There's also the Friedman test. Both of these are examples of frequency analysis
"""

if __name__ == "__main__":
    print("# CAESAR KEY SPACE ##########################")
    encrypted = caesar("secret{cRack_m3e_pLEaSe}", 12)
    print(crack_caesar(encrypted))
