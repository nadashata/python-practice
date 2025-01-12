letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

import random

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# ##Ordered Way
# ##if we need to generate password chars based on this exact order letters then symbols then numbers
# generated_pass=""
# for letter_count in range(0,nr_letters):
#     generated_pass = generated_pass + random.choice(letters)
# for symbols_count in range(0,nr_symbols):
#     generated_pass = generated_pass + random.choice(symbols)
# for numbers_count in range(0,nr_numbers):
#     generated_pass = generated_pass + str(random.choice(numbers))
# print(f"Your Password is:\n{generated_pass}")

# ##Shuffled Password
# ##if we need to generate password from non-ordered mix of letters & symbols & numbers
generated_pass=[]
for letter_count in range(0,nr_letters):
    generated_pass.append(random.choice(letters))
for symbols_count in range(0,nr_symbols):
    generated_pass.append(random.choice(symbols))
for numbers_count in range(0,nr_numbers):
    generated_pass.append(str(random.choice(numbers)))

# Randomly shuffle The password List
random.shuffle(generated_pass)

#print(f"Your Password is:\n{generated_pass}")
# Transform generated password from List format to string
resulted_pass=''
for char in generated_pass:
    resulted_pass += char

print(f"Your Password is:\n{resulted_pass}")
