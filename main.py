'''Практическое задание 3'''
'''Создание генератора чисел Фибоначчи на Python'''

#!usr/bin/env/python3
# -*- coding: utf-8 -*-

def nfib(n):
    l1 = [1, 1]
    i = 0
    while i < n - 2:
        l1.append(l1[i] + l1[i + 1])
        i += 1
    return l1


print(f'Список из 20 чисел Фибоначчи с помощью функции list(): {list(nfib(20))}')

print(f'Список из 20 чисел Фибоначчи с помощью генератора списка: {[k for k in nfib(20)]}')

l2 = []
for i in nfib(20):
    l2.append(i)
print(f'Список из 20 чисел Фибоначчи с помощью цикла for: {l2}')

print(f'Список из 20 чисел Фибоначчи с помощью генератора множества: ', sorted({j for j in nfib(20)}))









