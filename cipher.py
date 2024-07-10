from logo import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v','w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v','w', 'x', 'y', 'z']
print(logo)
def caesar(text_input, shift_input, direction_input):
        if direction_input == 'encode':
            cipher_text = ""
            for letter in text_input:
                if letter in alphabet:
                    position = alphabet.index(letter)
                    new_position = position + shift_input
                    new_letter = alphabet[new_position]
                    cipher_text += new_letter
                else:
                    cipher_text += letter
            print(f"The encoded message is {cipher_text}")

        elif direction_input == 'decode':
            cipher_text2 = ""
            for letter in text_input:
                if letter in alphabet:
                    position = alphabet.index(letter)
                    new_position = position - shift_input
                    new_letter = alphabet[new_position]
                    cipher_text2 += new_letter
                else:
                    cipher_text2 += letter
            print(f"The decoded message is {cipher_text2}")


flag = True
while flag:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text_input=text, shift_input=shift, direction_input=direction)
    answer = input("Type 'yes' to continue and 'no' to stop\n").lower()
    if answer == 'no':
        flag = False
    elif answer == 'yes':
        flag = True