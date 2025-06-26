def P(C:str, K:int, encrypt:bool) -> str:
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    decoded_msg = ""
    
    for encoded_letter in C.upper():
        if encoded_letter in alphabet:
            current_index = alphabet.find(encoded_letter)
            # Determines direction of the shift
            if encrypt: # Right shift (encryption)
                decoded_letter_index = (current_index + K) % len(alphabet)
            else: # Left shift (decryption)
                decoded_letter_index = (current_index - K) % len(alphabet)
            decoded_msg += alphabet[decoded_letter_index]
        else:
            decoded_msg += encoded_letter

    return decoded_msg

if __name__ == "__main__":
    direction = input("Encrypt? y/n: ")
    k = int(input("Enter shift size: "))
    c = input("Enter message: ")

    if direction.lower() == "y":
       msg = P(c, k, encrypt=True)
    elif direction.lower() == "n":
       msg = P(c, k, encrypt=False)

    print(msg)