# Password Generator
print("'Password Generator'")

user_input = int(input('Enter the password length : '))

import random
lower_case = 'abcdefghijklmnopqrstuvwxyz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '{}?@!$%^&()_+*'
all = lower_case+upper_case+numbers+symbols

for i in range(1):
    password = ' '.join(random.sample(all,user_input))
    print('Display the password :',password)