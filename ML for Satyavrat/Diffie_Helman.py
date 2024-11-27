import random

def modulus(base, expo, mod):
    return pow(base, expo, mod)

def generate_key():
    return random.randint(1, 100)

def xor(message, key):
    return ''.join(chr(ord(c) ^ key) for c in message)

if __name__ == '__main__':
    p = int(input("Enter a prime number: "))
    g = int(input("Enter a base: "))

    # Generate keys
    private_A, private_B = generate_key(), generate_key()
    pub_A, pub_B = modulus(g, private_A, p), modulus(g, private_B, p)

    # Calculate shared secrets
    shared_A, shared_B = modulus(pub_B, private_A, p), modulus(pub_A, private_B, p)

    print(f"\nUser A - private: {private_A}, Public: {pub_A}")
    print(f"User B - private: {private_B}, Public: {pub_B}")

    if shared_A == shared_B:
        print(f"\nShared secret: {shared_A}")
        message = input("Enter message: ")
        
        encrypted = xor(message, shared_A)
        print(f"Encrypted message: {encrypted}")
        
        decrypted = xor(encrypted, shared_B)
        print(f"Decrypted message: {decrypted}")
    else:
        print("Shared secrets do not match.")
