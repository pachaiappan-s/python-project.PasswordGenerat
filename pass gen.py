import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = "!@$%/"


all_char = lower + upper + number + symbol

leng = int(input("Enter length: "))

if leng < 3:
    print("Password length must be at least 3 to include all types.")
else:
  
    password = [
        random.choice(lower + upper),
        random.choice(number),
        random.choice(symbol)
    ]

    password += random.choices(all_char, k=leng - 3)
    
  
    random.shuffle(password)
    
    print("GENERATE PASSWORD:", "".join(password))
