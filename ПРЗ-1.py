import random
import string

def generate_random_password(length=8):
    # Символы, которые будут использоваться при генерации пароля
    characters = string.ascii_letters + string.digits + string.punctuation
    # Генерируем случайный пароль заданной длины
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Пример использования:
password_length = int(input("Введите длину пароля (по умолчанию 8): "))
if password_length <= 0:
    password_length = 8

random_password = generate_random_password(password_length)
print("Случайный пароль:", random_password)

import random

chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
number = input('количество паролей?'+ "\n")
length = input('длина пароля?'+ "\n")
number = int(number)
length = int(length)
for n in range(number):
    password =''
    for i in range(length):
        password += random.choice(chars)
    print(password)
print()
