# Learning Cryptography: From Toy Ciphers to AES

This roadmap builds intuition first, then moves toward real modern ciphers.

---

## 1. Toy Ciphers (Build Intuition)
Implement these completely.

- **Caesar / Shift Cipher**
- **Affine Cipher**
- **Vigenère Cipher**

What you should learn:
- Key space size
- Frequency analysis
- Why key reuse breaks security

---

## 2. Classical but Structured Ciphers
These introduce real mathematical structure.

- **Playfair Cipher**
- **Hill Cipher**
  - Linear algebra over modular arithmetic
  - Demonstrates why linear ciphers fail
- **One-Time Pad**
  - Perfect secrecy
  - Shows why key reuse is catastrophic

---

## 3. Feistel Networks (Major Conceptual Leap)
This is where modern block ciphers begin.

Implement a Feistel cipher using:
- XOR
- Substitution tables
- Permutations

Learn:
- Confusion vs diffusion
- Why encryption and decryption are symmetric
- Avalanche effect

---

## 4. Substitution–Permutation Networks (SPN)
This is the design family AES belongs to.

Build a small SPN with:
- 4-bit or 8-bit S-boxes
- Bit or byte permutations
- Multiple rounds

Learn:
- Why nonlinearity matters
- Basic intuition behind linear and differential cryptanalysis

---

## 5. DES (Historical, Not Secure)
A full real-world cipher.

Teaches:
- Large-scale Feistel design
- Key schedule construction
- Why S-box design is difficult

---

## 6. AES (Modern Baseline)
At this point AES should feel principled, not arbitrary.

Focus on:
- State representation
- Key schedule
- SubBytes / ShiftRows / MixColumns
- Finite field arithmetic (GF(2^8))

---

## 7. Modes of Operation & Authentication
Block ciphers alone are not secure systems.

Study:
- ECB (and why it fails)
- CBC, CTR
- **AEAD modes**: GCM, ChaCha20-Poly1305

Learn:
- IV / nonce requirements
- Padding issues
- Nonce misuse attacks

---

## 8. Stream Ciphers and MACs
Complete the picture.

- RC4 (broken but educational)
- ChaCha20
- Poly1305
- HMAC

---

## How to Study Effectively
- Implement in **Python first**, then C
- Always test against known vectors
- Try to break your own constructions
- Keep implementations small and readable

---

## Recommended Resources
- **CryptoPals challenges** (hands-on learning)
- *Understanding Cryptography* — Paar & Pelzl
- NIST specifications (after intuition is built)

---

## Goal
Learn *why* ciphers work before trusting ones that do.

