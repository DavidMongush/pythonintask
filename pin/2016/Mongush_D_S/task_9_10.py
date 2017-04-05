# Задание 9. Вариант 10.
# Mongush D.S.

# 05.04.17

import random
count = 0
WORDS = ("Компьютер", "Интернет", "Машина", "Программа")
win = random.choice(WORDS)

print("Слово выбрано, в нем", len(win), "букв. У тебя 5 попыток, чтобы угадать его буквы.")

#Сначала даем попытки угадать буквы слова
while count < 5:
    count += 1
    guessChar = input("Твой ход: ")
    if guessChar.lower() in win.lower() and guessChar != "":
        print("Да")
    else:
        print("Нет")

#Как только попытки исчерпаны, предоставляем возможность угадать слово
guessWord = input("Пора угадывать: ")
if guessWord == win:
    print("Поздравляем! Вы победили!")
else:
    print("Вы не угадали!")

input("\n\nЖми Enter ")

