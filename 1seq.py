amount_elements = int(input('Введите количество элементов списка: '))
list = []

for i in range(amount_elements):
        list.append(int(input(f'Введите {i+1} элемент: ')))

list.sort()
print(list)