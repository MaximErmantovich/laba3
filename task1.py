# Создать программный файл F1 в текстовом формате, записать в него
# построчно данные, вводимые пользователем. Об окончании ввода данных
# будет свидетельствовать пустая строка. Скопировать из файла F1 в файл F2
# строки, начиная с N до K. Подсчитать количество согласных букв в файле F2

F1 = open('files/laba1_F1.txt', 'w')
F2 = open('files/laba1_F2.txt', 'w')
print("Введите текст : ")
print("Для завершения ввода текста набери строку — 'Стоп'")
count = 0
list1 = []
while True:
    text = input()
    if text.lower() == 'стоп' or text.lower() == 'stop':
        break
    F1.write(text + '\n')
    list1.append(text)
    count += 1
while True:
    n = int(input("Введите n: "))
    k = int(input("Введите k: "))
    if n > k or n < 0 or k > count or n > count:
        print('Введите значения заново')
    else:
        break
count = 0
for i in range(n, k + 1):
    F2.write(list1[i-1] + '\n')
    for j in range(len(list1[i])):
        if list1[i][j].lower() in 'бвгджзйклмнпрстфхцчшщbcdfghklmnpqrstvxz':
            count += 1
print(f'Количество согласных букв во втором файле — {count}')

F1.close()
F2.close()

