import random
letters = ['a', 'b','c', 'd', 'g' 'k', 'e' 'p' 'h', 'l','s' ]
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','#', '$','%','&','*','+']

print("Welcome to tge PyPassword Genarator!")
nr_letters =int(input("How many letters would you like in your password? \n"))
nr_symbols =int(input(f"How many symbols would you like?\n"))
nr_numbers =int(input(f"How many numbers would you like?\n"))

password = ""

for char in range(1, nr_letters +1):
    password += random.choice(letters)

for char in range(1, nr_symbols +1):
    password += random.choice(symbols)

for char in range(1, nr_numbers +1):
    password += random.choice(numbers)
print(password)
