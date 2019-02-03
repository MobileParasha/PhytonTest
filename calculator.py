def calc(a, b, op):
   

    if op not in '+-/*':
        return 'Пожалуйста выбирайте только из этого: "+, -, *, /"!'

    if op == '+':
        return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a + b))
    if op == '-':
        return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a - b))
    if op == '*':
        return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a * b))
    if op == '/':
        return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a / b))


def main():  # Wrapper function

    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    op = input(
        'Какую операцию вы хотите сделать?\
        \nВыбирайте между "+, -, *, /" : ')

    print(calc(a, b, op))

if __name__ == '__main__':
    main()
