import operators
for k in range(1000000):
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

    an=int(input("Хочите продовжити:\n1-так,2-ні\n"))
    if an == 2:
        print('Дякуємо, що скористалися нашим калькулятором! :)')
        break
