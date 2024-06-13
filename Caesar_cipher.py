task = input("Type 'encrypt' for encryption and 'decrypt' for decryption: \n")
text = input("Type keyword/phrase: \n")
shift = int(input("Enter Shift key: \n"))

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphabet2 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def encryption(plain_text, shift_key):
    cipher_text = ""
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_key) % 26
            cipher_text += alphabet[new_position]

        elif char in alphabet2:
            position = alphabet2.index(char)
            new_position = (position + shift_key) % 26
            cipher_text += alphabet2[new_position]

        else:
            cipher_text += char
    print(f"Encrypted text: {cipher_text}")


def decryption(cipher_text, shift_key):
    plain_text = ""
    for char in cipher_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position - shift_key) % 26
            plain_text += alphabet[new_position]

        elif char in alphabet2:
            position = alphabet2.index(char)
            new_position = (position - shift_key) % 26
            plain_text += alphabet2[new_position]

        else:
            plain_text += char
    print(f"Decrypted text: {plain_text}")


if task == "encrypt":
    encryption(plain_text=text, shift_key=shift)
elif task == "decrypt":
    decryption(cipher_text=text, shift_key=shift)
