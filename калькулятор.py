import operators

#numbers and operators
a=int(input("Введіть перше число:\n"))
b=input("Введіть дію (+, -, *, /):\n")
c=int(input("Введіть друге число:\n"))

#actions and result
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
