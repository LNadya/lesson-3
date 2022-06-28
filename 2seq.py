elements = list(map(int, input('Введите элементы списка через запятую: ').split(',')))
elements = set(elements)
print(*list(elements), sep=', ')