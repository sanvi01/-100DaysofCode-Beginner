alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
mssg = input("Type message:\n").lower()
shift = int(input("Type the shift number:\n"))

def cipher(start_mssg, shift_amount, cipher_direction):
    end_mssg = ""
    if cipher_direction == 'decode':
        shift_amount *= -1
    for letter in mssg:
        org_position = alphabet.index(letter)
        new_position = org_position + shift_amount
        end_mssg += alphabet[new_position]
    print(f"The {cipher_direction}d message is: {end_mssg}")

cipher(start_mssg = mssg, shift_amount = shift, cipher_direction = direction)  
