import string #пожключение библитоеки для операций со строками
import random #подключение библиотеки для генерации случайных чисел
my_number = 1000
while True: #проверка на условие задания №1
    print("Введите число")
    user_number = int(input())
    if user_number > my_number:
        break
print("Ввод окончен")

some_list = ['red', 'blue', 'rule', '1red'] #исходный список их строк
print("Исходный список", some_list)
for some_str in some_list:
    if some_str[0] == 'r': #проверка на начало с символа 'r'
        print(some_str)
print("Сгенерированная случайная строка по заданию:")
some_str = ''
some_seq = string.ascii_letters + string.digits
 
for i in range(8):
    some_str += random.choice(some_seq)
 
if some_str.isalpha():
    some_str[random.randint(0,7)] = random.choice(string.digits) 
print(some_str)

orig_str = 'i want 3 cows and 5 birds' #исходная строка для задания №4
print("Исходная строка: ")
print(orig_str)
new1 = ''
new2 = '' 
for char in orig_str:
    if char.isalpha():
        new1 += char
    if char.isdigit():
        new2 += char 
print("Первая строка: ")
print(new1)
print("Вторая строка: ")
print(new2)
