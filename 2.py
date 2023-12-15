# перебираем элементы через вложенные циклы for

# находим сумму элементов двумерного списка (способ 1)
data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
summa=0
for line in data :
    for elem in line:
        summa += elem
        print(summa)