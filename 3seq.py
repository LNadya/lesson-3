list1 = set(map(int, input('Введите элементы 1-го списка: ').split(',')))
list2 = set(map(int, input('Введите элементы 2-го списка: ').split(',')))
print(*(list1-list2), sep=', ')