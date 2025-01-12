letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

import random

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


generated_pass=""
pass_len = nr_letters + nr_symbols + nr_numbers
for count_pass_char in range(0,pass_len):
    char_order = random.randint(0,2) # 0 letter, 1 for symbol, 2 for number
    if char_order == 0 and nr_letters > 0:
        nr_letters -=1
        generated_pass = generated_pass + random.choice(letters)
    elif char_order == 1 and nr_symbols > 0:
        nr_symbols -=1
        generated_pass = generated_pass + random.choice(symbols)
    elif char_order == 2 and nr_numbers > 0:
        nr_numbers -=1
        generated_pass = generated_pass + str(random.choice(numbers))
    elif char_order == 0 and nr_letters <= 0:
        if nr_symbols > 0:
            nr_symbols -= 1
            generated_pass = generated_pass + random.choice(symbols)
        else:
            nr_numbers -= 1
            generated_pass = generated_pass + str(random.choice(numbers))
    elif char_order == 1 and nr_symbols <= 0:
        if nr_letters > 0:
            nr_letters -= 1
            generated_pass = generated_pass + random.choice(letters)
        else:
            nr_numbers -= 1
            generated_pass = generated_pass + str(random.choice(numbers))
    else:
        if nr_symbols > 0:
            nr_symbols -= 1
            generated_pass = generated_pass + random.choice(symbols)
        else:
            nr_letters -= 1
            generated_pass = generated_pass + random.choice(letters)

print(f"Your password is :\n{generated_pass}")
