#star
n="\033[1mКалькулятор"
n1=n.center(70)
print(n1)


#valuta
Usd=41.45
Eur=48.45
Pln=11.3


#calculator
import operators
while True:
    v=input("Оберіть дію: 1-калькулятор, 2-перевод валют, 3-вийти\n")
    if v=="1":
            try:
                a=int(input("Введіть перше число:\n"))
                b=input("Введіть дію (+, -, *, /):\n")
                c=int(input("Введіть друге число:\n"))

                print("Результат:")
                if b=="+":
                    print(operators.plus(a,c))
                elif b=="-":
                    print(operators.minus(a,c))
                elif b=="*":
                    print(operators.multiply(a,c))
                elif b=="/":
                    if c != 0:
                        print(operators.divide(a,c))
                    else:
                        print('\033[31m\033[1mНа нуль не можна ділити!\033[0m\033[0m')
                else:
                    print("Ми не маємо такої дії :(")
            except ValueError:
                print('Вводьте числа, а не букви і знаки!')

            an=int(input("Хочите продовжити:\n1-так,2-ні\n"))
            if an == 2:
                v = input("Оберіть дію: 1-калькулятор, 2-перевод валют, 3-вийти\n")



#request
    elif v=="2":
            try:
                r=input('Оберіть валюту: 1-USD, 2-EUR, 3-PLN\n')
                if r=='1':
                    a=float(input('Введіть суму в гривнях: '))
                    print(a/Usd)
                elif r=='2':
                    a=float(input('Введіть суму в гривнях: '))
                    print(a/Eur)
                elif r=='3':
                    a=float(input('Введіть суму в гривнях: '))
                    print(a/Pln)
            except ValueError:
                print('Вводіть числа, а не букви і знаки!')
            an = int(input("Хочите продовжити:\n1-так,2-ні\n"))
            if an == 2:
                print('Дякуємо, що скористалися нашим калькулятором! :)')
                break
    elif v == 3:
        print('Дякуєм, що скористалися нашим калькулятором')
        break



