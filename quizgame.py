score = 0
an1 = 'Київ'
an = input('Столиця України\n')
if an == an1:
    print('Вірно :)')
    score += 1
else:
    print('Не вірно :(')
    score -= 1

an2 = 'Лондон'
pn = input('Столиця Великої Британії\n')
if pn == an2:
    print('Вірно :)')
    score += 1
else:
    print('Не вірно :(')
    score -= 1

an3 = 'Вашингтон'
pr = input('Столиця США\n')
if pr == an3:
    print('Вірно :)')
    score += 1
else:
    print('Не вірно :(')
    score -= 1

an4 = 'Берлін'
pr4 = input('Столиця Німеччини\n')
if pr4 == an4:
    print('Вірно :)')
    score += 1
else:
    print('Не вірно :(')
    score -= 1

an5 = 'Париж'
pr5 = input('Столиця Франції\n')
if pr5 == an5:
    print('Вірно :)')
    score += 1
else:
    print('Не вірно :(')
    score -= 1

an6 = 'Рим'
pr6 = input('Столиця Італії\n')
if pr6 == an6:
    print('Вірно :)')
    score += 1
else:
    print('Не вірно :(')
    score -= 1

an7 = 'Мадрид'
pr7 = input('Столиця Іспанії\n')
if pr7 == an7:
    print('Вірно :)')
    score += 1
else:
    print('Не вірно :(')
    score -= 1
an8 = 'Оттава'
pr8 = input('Столиця Канади\n')
if pr8 == an8:
    print('Вірно :)')
    score += 1
else:
    print('Не вірно :(')
    score -= 1

an9 = 'Стокгольм'
pr9 = input('Столиця Швеції\n')
if pr9 == an9:
    print('Вірно :)')
    score += 1
else:
    print('Не вірно :(')
    score -= 1

an10 = 'Каїр'
pr10 = input('Столиця Єгипту\n')
if pr10 == an10:
    print('Вірно :)')
    score += 1
else:
    print('Не вірно :(')
    score -= 1

print(f'\nТест завершено! Ви набрали {score} з 10 балів.')