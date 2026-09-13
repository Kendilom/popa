need_H = input('Введи слово с буквой h/H или умрешь ;3\n')
while True:
    if 'h' in need_H or 'H' in need_H:
        print('Маладец')
        break
    else:
        need_H = input('Неправильно еще раз: \n')
        continue