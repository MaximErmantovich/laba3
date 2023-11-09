# -*- coding: cp1251 -*-
# Сформировать (не программно) текстовый файл. В нём каждая
# строка должна описывать учебный предмет и наличие лекционных,
# практических и лабораторных занятий по предмету. Сюда должно входить и
# количество занятий. Необязательно, чтобы для каждого предмета были все
# типы занятий.
# Сформировать словарь, содержащий название предмета и общее
# количество занятий по нему. Вывести его на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) 10(лаб)
# Физкультура: 30(пр)

file = open('files/laba1_task3.txt', 'w')
dictionary = {'Информатика': 0, 'Физика': 0,
              'Физкультура': 2, "Математика": 0, 'История': 0, 'Английский': 0}
print("Для завершения ввода текста набери строку — 'Стоп'")
while True:
    print('Введите наименование занятия:')
    name = input()
    if name in dictionary.keys():
        while True:
            lk = int(input('Введите сколько часов (лк) '))
            pz = int(input('Введите сколько часов (пз) '))
            lab = int(input('Введите сколько часов (лаб) '))
            if lab + pz + lk == dictionary[f'{name}']:
                if lab == 0:
                    if pz == 0:
                        file.write(f'{name}: {lk}(л)' + '\n')
                    elif lk == 0:
                        file.write(f'{name}: {pz}(пр) ' + '\n')
                    else:
                        file.write(f'{name}: {lk}(л) {pz}(пр)' + '\n')
                elif pz == 0:
                    if lk == 0:
                        file.write(f'{name}: {lab}(лаб)' + '\n')
                    else:
                        file.write(f'{name}: {lk}(л) {lab}(лаб)' + '\n')
                elif lk == 0:
                    file.write(f'{name}: {pz}(пр) {lab}(лаб)' + '\n')
                else:
                    file.write(f'{name}: {lk}(л) {pz}(пр) {lab}(лаб)'+'\n')
                break
            else:
                print('Введите правильно количество часов')
    else:
        if name.lower() == 'стоп' or name.lower() == 'stop':
            break
        else:
            print('Введите наименование занятия правильно')
file.close()
with open("files/laba1_task3.txt", "r") as file:
    for line in file:
        data = line.strip().split()
