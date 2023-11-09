# -*- coding: cp1251 -*-
# Создать вручную и заполнить несколькими строками текстовый
# файл, в котором каждая строка будет содержать данные о фирме: название,
# форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой
# компании, а также среднюю прибыль. Если фирма получила убытки, в расчёт
# средней прибыли её не включать.Далее реализовать список. Он должен содержать словарь с фирмами и
# их прибылями, а также словарь со средней прибылью. Если фирма получила
# убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий
# файл.
# Пример json-объекта: [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit":2000}]
import json

# print(eval(input()))

firm_list = []

with open("files/laba1_task4.txt", "r") as file:
    for line in file:
        data = line.strip().split()
        name = data[0]
        ownership = data[1]  # владелец
        revenue = int(data[2])  # Доходы
        expenses = int(data[3])  # Расходы
        profit = revenue - expenses
        firm_list.append({name: profit})

total_profit = 0
profitable_firms = 0

for firm in firm_list:
    for name, profit in firm.items():
        if profit > 0:
            total_profit += profit
            profitable_firms += 1

average_profit = total_profit / profitable_firms

firm_list.append({"average_profit": average_profit})

with open("files/my_file.json", "w") as write_f:
    json.dump(firm_list, write_f)
