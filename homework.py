print('STARTSWITH')
a=input("Вкажіть своє ім'я\n")
b=int(input("Вкажіть свій вік\n"))
text=f'Вітаємо {a}! Вас зареєстровано з віком {b}.'
print(text.startswith(f'Вітаємо {a}'))
print(text.startswith(f'{b}'))

print('CAPITALIZE')
a1=input("Як вас звати?\n")
t=f'{a1}, ви впевнені, що хочите продовжити?'
print(t.capitalize())
