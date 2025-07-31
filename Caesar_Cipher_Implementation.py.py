def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

while True:
    print("\n--- Caesar Cipher ---")
    choice = input("Do you want to encrypt or decrypt? (e/d): ").strip().lower()

    if choice not in ['e', 'd']:
        print("Invalid choice. Please enter 'e' to encrypt or 'd' to decrypt.")
        continue

    text = input("Enter the text: ")
    try:
        shift = int(input("Enter the shift key (number): "))
    except ValueError:
        print("Invalid shift. Please enter a number.")
        continue

    if choice == 'e':
        result = encrypt(text, shift)
        print("Encrypted Text:", result)
    else:
        result = decrypt(text, shift)
        print("Decrypted Text:", result)

    cont = input("Do you want to continue? (yes/no): ").strip().lower()
    if cont != 'yes':
        print("Exiting Caesar Cipher. Goodbye!")
        break
