import string
import math

def reverse_cipher(message):
    temp = list('')
    for i in message:
        temp.append(i)
    temp.reverse()
    ciphered = ''.join(temp)
    print (ciphered)

def reverse_decipher(message):
    temp = list('')
    for i in message:
        temp.append(i)
    temp.reverse()
    deciphered = ''.join(temp)
    print(deciphered)

def caeser_cipher(sentence, number):
    ciphered = []
    for char in sentence:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            ciphered.append(chr((ord(char) - base + number) % 26 + base))
        else:
            ciphered.append(char)
    print(''.join(ciphered))

def caesar_decipher(sentence, number):
    deciphered = []
    for char in sentence:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            deciphered.append(chr((ord(char) - base - number) % 26 + base))
        else:
            deciphered.append(char)
    print(''.join(deciphered))

def caesar_bruteforce(sentence):
    ciphered = list(sentence)
    deciphered = []

    for number in range(26):
        for j in ciphered:
            if j.isalpha():
                base = ord('A') if j.isupper() else ord('a')
                deciphered.append(chr((ord(j) - base - number) % 26 + base))
            else:
                deciphered.append(j)

        new_sentence = ''.join(deciphered)
        print(f"key {number}: {new_sentence}")
        deciphered.clear()

def affine_cipher(sentence, key1, key2):
    letters_to_num = {char: idx for idx, char in enumerate(string.ascii_letters)}
    num_to_letters = {idx: char for idx, char in enumerate(string.ascii_letters)}

    deciphered = list('')
    for i in sentence:
        deciphered.append(i)

    ciphered = list('')
    for j in deciphered:
        if j != ' ':
            first =(letters_to_num[j] * key1 + key2) % 26
            ciphered.append(num_to_letters[first])

        else:
            ciphered.append(j)

    new_sentence = ''.join(ciphered)
    print (new_sentence)

def affine_decipher(sentence, key1, key2):
    letters_to_num = {char: idx for idx, char in enumerate(string.ascii_letters)}
    num_to_letters = {idx: char for idx, char in enumerate(string.ascii_letters)}

    ciphered = list('')
    for i in sentence:
        ciphered.append(i)

    mod_inverse = pow(key1, -1, 26)

    deciphered = list('')
    for j in ciphered:
        if j != ' ':
            first = ((letters_to_num[j] - key2) * mod_inverse) % 26
            deciphered.append(num_to_letters[first])

        else:
            deciphered.append(j)

    new_sentence = ''.join(deciphered)
    print(new_sentence)


def affine_bruteforce(sentence):
    def key1_values():
        return [k for k in range(1,26) if math.gcd(k,26) == 1]

    letters_to_num = {char: idx for idx, char in enumerate(string.ascii_letters)}
    num_to_letters = {idx: char for idx, char in enumerate(string.ascii_letters)}

    ciphered = list('')
    for i in sentence:
        ciphered.append(i)

    deciphered = list('')
    possible_values = key1_values()

    for key1 in possible_values:
        mod_inverse = pow(key1, -1, 26)
        for key2 in range(26):
            for j in ciphered:
                if j != ' ':
                    first = ((letters_to_num[j] - key2) * mod_inverse) % 26
                    deciphered.append(num_to_letters[first])

                else:
                    deciphered.append(j)

            new_sentence = ''.join(deciphered)
            print(f"key1 = {key1} and key2 = {key2}: {new_sentence}")
            deciphered.clear()

def simple_substitution_cipher(message, key):
    alphabet = string.ascii_letters
    encrypted = ''
    for char in message:
        if char in alphabet:
            index = alphabet.index(char)
            encrypted += key[index]
        else:
            encrypted += char
    print(encrypted)

def simple_substitution_decipher(message, key):
    alphabet = string.ascii_letters
    decrypted = ''
    for char in message:
        if char in key:
            index = key.index(char)
            decrypted += alphabet[index]
        else:
            decrypted += char
    print(decrypted)

def vigenere_cipher(message, key):
    alphabet=string.ascii_letters
    key_index = 0
    encrypted = ''
    for char in message:
        if char in alphabet:
            index = alphabet.index(char)
            index2 = alphabet.index(key[key_index % len(key)])
            rakam = (index + index2) % 26
            encrypted += alphabet[rakam]
        else:
            encrypted += char
        key_index+=1
    print (encrypted)

def vigenere_decipher(message, key):
    alphabet = string.ascii_letters
    key_index = 0
    decrypted = ''
    for char in message:
        if char in alphabet:
            index = alphabet.index(char)
            index2 = alphabet.index(key[key_index % len(key)])
            rakam = (index - index2 + 26) % 26
            decrypted += alphabet[rakam]
        else:
            decrypted += char
        key_index += 1
    print(decrypted)

def main():
    while True:
        print("\n--- Choose Cipher Type ---")
        print("1. Reverse Cipher")
        print("2. Caesar Cipher")
        print("3. Affine Cipher")
        print("4. Simple Substitution Cipher")
        print("5. Vigenère Cipher")
        print("0. Exit")

        cipher_choice = input("Enter your choice: ")

        if cipher_choice == "1":
            print("\n--- Reverse Cipher ---")
            print("1. Cipher")
            print("2. Decipher")
            sub_choice = input("Enter your choice: ")

            msg = input("Enter your message: ")
            if sub_choice == "1":
                reverse_cipher(msg)
            elif sub_choice == "2":
                reverse_decipher(msg)
            else:
                print("Invalid choice.")

        elif cipher_choice == "2":
            print("\n--- Caesar Cipher ---")
            print("1. Cipher")
            print("2. Decipher")
            print("3. Bruteforce")
            sub_choice = input("Enter your choice: ")

            msg = input("Enter your message: ")
            if sub_choice == "1":
                shift = int(input("Enter the shift number: "))
                caeser_cipher(msg, shift)
            elif sub_choice == "2":
                shift = int(input("Enter the shift number: "))
                caesar_decipher(msg, shift)
            elif sub_choice == "3":
                caesar_bruteforce(msg)
            else:
                print("Invalid choice.")

        elif cipher_choice == "3":
            print("\n--- Affine Cipher ---")
            print("1. Cipher")
            print("2. Decipher")
            print("3. Bruteforce")
            sub_choice = input("Enter your choice: ")

            msg = input("Enter your message: ")
            if sub_choice == "1":
                key1 = int(input("Enter key1 (coprime with 26): "))
                key2 = int(input("Enter key2: "))
                affine_cipher(msg, key1, key2)
            elif sub_choice == "2":
                key1 = int(input("Enter key1 (coprime with 26): "))
                key2 = int(input("Enter key2: "))
                affine_decipher(msg, key1, key2)
            elif sub_choice == "3":
                affine_bruteforce(msg)
            else:
                print("Invalid choice.")

        elif cipher_choice == "4":
            print("\n--- Simple Substitution Cipher ---")
            print("1. Cipher")
            print("2. Decipher")
            sub_choice = input("Enter your choice: ")

            msg = input("Enter your message: ")
            key = input("Enter 52-letter key (uppercase + lowercase): ")

            if sub_choice == "1":
                simple_substitution_cipher(msg, key)
            elif sub_choice == "2":
                simple_substitution_decipher(msg, key)
            else:
                print("Invalid choice.")

        elif cipher_choice == "5":
            print("\n--- Vigenère Cipher ---")
            print("1. Cipher")
            print("2. Decipher")
            sub_choice = input("Enter your choice: ")

            msg = input("Enter your message: ")
            key = input("Enter the key (letters only): ")

            if sub_choice == "1":
                vigenere_cipher(msg, key)
            elif sub_choice == "2":
                vigenere_decipher(msg, key)
            else:
                print("Invalid choice.")

        elif cipher_choice == "0":
            print("Exiting program...")
            break

        else:
            print("Invalid cipher choice.")

main()
