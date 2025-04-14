import random

print("Welcome To Your Password Generator")

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?.,0123456789' #This is a string of all characters you want to include in your password

number = input('Amount of password to generate: ')
number = int(number)

length = input('Input Your password length: ')
length = int(length)

print('\nhere are your passwoeds:')

for pwd in range (number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars) #adding random.choice to this password variable set there
    print(passwords)