import string
import random

alphabeth = list(string.ascii_letters)
numbers = list(string.digits)
punctutation = list(string.punctuation)
list_of_alphameric = [alphabeth, numbers, punctutation]

def generate_password(strs, count):
    new_list = [random.choice(strs) for i in range(count)]
    return new_list

def create_list_of_passwords(list1, list2):
    password = []
    for i in list1:
        for j in list2:
            passwords = generate_password(i, j)
        password += passwords
    return password

print("Welcome to PyPassword Generator!")
continue_generating = True
while continue_generating:
    num_of_letters = int(input("How many letters would you like in your password? "))
    num_of_numbers = int(input("How many numbers would you like? "))
    num_of_symbols = int(input("How many symbols would you like? "))
    list_of_counts = [num_of_letters, num_of_numbers, num_of_symbols]

    password = create_list_of_passwords(list_of_alphameric, list_of_counts)
    
    random.shuffle(password)
    print(f'Here is your password: {"".join(password)}')
    generate_another_password = input("Would you like to generate another password? Y/N : ").lower()
    if generate_another_password != "y":
        continue_generating = False