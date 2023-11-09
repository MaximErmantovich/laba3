# -*- coding: cp1251 -*-
# Создать текстовый файл (не программно). Построчно записать
# фамилии студентов и оценки по 5 предметам (не менее 10 строк). Высчитать
# средний балл каждого студента. Вывести на экран студентов, чей средний
# балл ниже 6.
# Пример файла:
# Иванов 8 8 7 6 5
# Петров 5 6 7 7 6
def average_grade(text):
    summ = 0
    for i in range(1, 6):
        summ += int(text[i])
    return (summ / 5)


file = open('files/laba1_task2.txt', 'w')
print("Введите текст : ")
print('Пример файла:\nИванов 8 8 7 6 5\nПетров 5 6 7 7 6')
print("Для завершения ввода текста набери строку — 'Стоп'")
list1 = []
while True:
    text = input()
    if text.lower() == 'стоп' or text.lower() == 'stop':
        break
    if len(text.split()) != 6:
        print('Введите текст заново')
        continue
    file.write(text+'\n')
    text = text.split()
    if average_grade(text) < 6:
        list1.append(' '.join(text))
print('Ученики у которых средний балл ниже 6')
for i in range(len(list1)):
    print(list1[i])
file.close()
