alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
while True:
    direction = input("What you want to do Encode or Decode ?\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    # Encoding

    if direction == "encode":
        def encode(plain_text, shift_amount):
            cipher_text = ""
            for letter in plain_text:
                position = alphabet.index(letter)
                new_position = position + shift_amount
                new_letter = alphabet[new_position]
                cipher_text += new_letter
            print(f"The Encoded text is {cipher_text}")
        encode(plain_text=text, shift_amount=shift)

    # Decoding

    elif direction == "decode":
        def decode(plain_text, shift_amount):
            cipher_text = ""
            for letter in plain_text:
                position = alphabet.index(letter)
                new_position = position - shift_amount
                new_letter = alphabet[new_position]
                cipher_text += new_letter
            print(f"The Decoded text is {cipher_text}")
        decode(plain_text=text, shift_amount=shift)
    play_again = input("Play Again Y/N ?\n")
    if play_again.lower() != 'y':
        break
