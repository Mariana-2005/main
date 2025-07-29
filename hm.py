import os



print('\033[1m---Програма для обліку справ---')

with open('C:/Users/user/Desktop/справи.txt', 'w', encoding="utf-8") as file:
    file.write('Купити продукти')

while True:
    menu=input('Оберіть:1-показати всі справи, 2-додати нову справу,3-очистити всі сапрви,4-вийти\n')
    if menu == '1' :
        with open('C:/Users/user/Desktop/справи.txt', 'r', encoding="utf-8") as file:
            text = file.read()
            print(text)
        if len(text) == 0 :
            print('Список порожній')
    elif menu == '2':
        s=input('\033[1mВведіть справу, яку ви хочите додати:\n')
        with open('C:/Users/user/Desktop/справи.txt', 'a', encoding="utf-8") as file:
            text = file.write('\n' + s)
            print(text)
            print("Справу додано!")
    elif menu == '3':
        with open('C:/Users/user/Desktop/справи.txt', 'w', encoding="utf-8") as file:
            pass
        print('Всі справи видалено')
    elif menu == '4':
        print("Вихід з програми...")
        break
    else:
        print('Error')
        break