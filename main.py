n = input('Укажите количество чисел: ')

def type_check(v):
    for i in v:
        if i.isalpha() or i in '., !@#$%ˆ&*()_+-={}[]><':
            return False
    return True

def nfib(t):
    l1 = [1, 1]
    i = 0
    while i < t - 2:
        l1.append(l1[i] + l1[i + 1])
        i += 1
    return l1

if type_check(n):
    print(f'Список из {int(n)} чисел Фибоначчи: {nfib(int(n))}')

    # Разные способы вывода результатов на экран:
    # print(f'Список из 20 чисел Фибоначчи с помощью функции list(): {list(nfib(int(n)))}')
    # ***
    # print(f'Список из 20 чисел Фибоначчи с помощью генератора списка: {[k for k in nfib(int(n))]}')
    # ***
    # l2 = []
    # for i in nfib(int(n)):
    #     l2.append(i)
    # print(f'Список из 20 чисел Фибоначчи с помощью цикла for: {l2}')
    # ***
    # print(f'Список из 20 чисел Фибоначчи с помощью генератора множества: ', sorted({j for j in nfib(int(n))}))
else:
    print('Некорректный ввод! Вводите только целые положительные числа')









