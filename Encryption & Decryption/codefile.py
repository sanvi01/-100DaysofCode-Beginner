alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def cipher(start_mssg, shift_amount, cipher_direction):
    end_mssg = ""
    if cipher_direction == 'decode':
        shift_amount *= -1
    for char in mssg:
        if char in alphabet:
            org_position = alphabet.index(char)
            new_position = org_position + shift_amount
            end_mssg += alphabet[new_position]
        else:
            end_mssg += char
    print(f"The {cipher_direction}d message is: {end_mssg}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    mssg = input("Type message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # %26 keeps in check that the index remains inside range of the alphabet list as it return remainder
    shift = shift % 26
    
    cipher(start_mssg = mssg, shift_amount = shift, cipher_direction = direction)        
    
    result = input("Type 'Yes' if you want to continue else type 'No'.").lower()
    if result == 'no':
        should_continue = False
        print("GoodBye")  
