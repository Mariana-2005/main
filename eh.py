import random


#початок
print('\033[1mВітаємо вас у грі Вдача\033[0m')
a=input('\033[1mЯк вас звати?\033[0m\n').title()
b=int(input(f'\033[1m{a}, введіть число від 1 до 10:\n\033[0m\n'))

#таємне число
c=random.randint(1, 10)

#перевірка
if b==c:
    print(c)
    print('\033[1mВАУ! Гарна інтуіція :)\033[0m')
else:
    print(c)
    print('\033[1mНу ти просто лох :)\033[0m')