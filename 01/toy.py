ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def char_cipher(text, func):
    out = []
    for c in text:
        if 'a' <= c <= 'z':
            out.append(chr(func(ord(c) - ord('a')) + ord('a')))
        elif 'A' <= c <= 'Z':
            out.append(chr(func(ord(c) - ord('A')) + ord('A')))
        else:
            out.append(c)
    return ''.join(out)

def char_cipher_positional(text, func):
    out = []
    for i, c in enumerate(text):
        if 'a' <= c <= 'z':
            out.append(chr(func(ord(c) - ord('a'), i) + ord('a')))
        elif 'A' <= c <= 'z':
            out.append(chr(func(ord(c) - ord('A'), i) + ord('A')))
        else:
            out.append(c)
    return ''.join(out)

def caesar(text, shift):
    """
    The Caesar cipher shifts the entire alphabet left or right by a
    certain number of positions.

    A ROT13 cipher is simply a caesar cipher where the shift is 13.
    """
    return char_cipher(text, lambda x: (x + shift) % 26)

def affine_encrypt(text, m, b):
    return char_cipher(text, lambda x: (m * x + b) % 26)

def modinv(a, m):
    """
    gcd(a, b) = gcd(b, a mod b)
    let a mod b be the (r)emainder. So first, keep replacing the pair until remainder is 0
    e.g. (48, 18) = (18, 48mod18=12)
         (18, 12) = (12, 6)
         (12,  6) = (6,  0)
    then the last nonzero remainder 6 equals gcd(48, 18)
    track x and y so gcd=x*a + y*m

    x*a+y*m=gcd(a, m) = 1 = 1(mod m)
    since y * m = 0 (mod m)
    then we have x*a=1(mod m) and x is the modular inverse of a

    (I don't really get this but I'll brush past for now)
    """
    t, newt = 0, 1 # coefficients for a
    r, newr = m, a # remainders
    while newr != 0:
        q = r // newr
        t, newt = newt, t - q * newt
        r, newr = newr, r - q * newr
    if r != 1:
        raise ValueError("no inverse")
    return t % m

def affine_decrypt(encrypted, m, b):
    m_inv = modinv(m, 26)
    return char_cipher(encrypted, lambda x: (m_inv * (x - b)) % 26)

def vigenere(text, key, is_decode=False):
    # vigenere might actually skip over non text characters but I'll just do this mod idea anyways
    key = key.lower()
    key = tuple((ord(c) - ord('a')) if not is_decode else (ord('a') - ord(c)) for c in key)
    keylen = len(key)
    func = lambda x, i: (x + key[i % keylen]) % 26
    return char_cipher_positional(text, func)

if __name__ == "__main__":
    encrypted= caesar(ALPHABET, 13)
    decrypted = caesar(encrypted, -13)
    assert decrypted == ALPHABET
    print(encrypted)

    encrypted = affine_encrypt(ALPHABET, 55, 12)
    decrypted = affine_decrypt(encrypted, 55, 12)
    assert decrypted == ALPHABET
    print(encrypted)

    encrypted = vigenere(ALPHABET, 'hello')
    decrypted = vigenere(encrypted, 'hello', True)
    assert decrypted == ALPHABET
    print(encrypted)