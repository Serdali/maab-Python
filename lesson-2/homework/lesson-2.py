# 1. Age Calculator (Write a Python program to ask for a user's name and year of birth, then calculate and display their age.)
name = input("Enter your name: ")
birth_year = int(input("Enter your year of birth: "))
age = 2025 - birth_year

print(f"Hello, {name}! You are {age} years old.")

# 2. Extract Car Names (Extract car names from the following text: txt = 'LMaasleitbtui')
txt = 'LMaasleitbtui'

print(txt[::2])
print(txt[1::2])

# 3. Extract Car Names (Extract car names from the following text: txt = 'MsaatmiazD')
txt = 'MsaatmiazD'

print(txt[::2])
print(txt[1::2][::-1])

# 4. Extract Residence Area (Extract the residence area from the following text: txt = "I'am John. I am from London" )
txt = "I'am John. I am from London"
t = txt.split()[-1]
print('Residence area is', t)

# 5. Reverse String (Write a Python program that takes a user input string and prints it in reverse order.)
txt = input('Write any string to reverse it: ')
print(f'Reverse of {txt} is',txt[::-1])

# 6. Count Vowels (Write a Python program that counts the number of vowels in a given string.)
txt = input('Enter any string: ')
print('Number of vowels ', sum(1 for i in txt if i.lower() in 'aeiou'))

# 7. Find Maximum Value (Write a Python program that takes a list of numbers as input and prints the maximum value.)
num = list(map(int, input('Enter number by space:').split()))
print('Max value is',max(num))

# 8. Check Palindrome (Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).)
word = input('Enter a word: ')

if word.lower() == word[::-1].lower():
    print("It's a palindrome")
else:
    print("It's not palindrome")

# 9. Extract Email Domain (Write a Python program that extracts and prints the domain from an email address provided by the user.)
email = input("Enter your email address: ")
domain = email.split('@')[1]
print('Email domain is',domain)

# 10. Generate Random Password (Write a Python program to generate a random password containing letters, digits, and special characters.)
import random
import string

def easy_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

print("Your password:", easy_password())