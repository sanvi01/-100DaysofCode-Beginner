# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import random
print("Welcom to pyPasword creator!")
password = []
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','@','#','$','%','^','&','*','(',')','+','-']

no_letters = int(input("How many letters do you want in you password?\n"))
no_nums = int(input("How many numbers do you want in your password?\n"))
no_symbols = int(input("How many symbols do you want in your password?\n"))


for i in range(0, no_letters):
    password.append(random.choice(letters))
  
for i in range(0, no_nums):
    password.append(random.choice(numbers))

for i in range(0, no_symbols):
    password.append(random.choice(symbols))

random.shuffle(password)
final_pass = ""    
for i in password:
    final_pass += i

print(f"Your password is: {final_pass})
    
