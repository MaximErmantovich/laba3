# -*- coding: cp1251 -*-
# ������� ������� � ��������� ����������� �������� ���������
# ����, � ������� ������ ������ ����� ��������� ������ � �����: ��������,
# ����� �������������, �������, ��������.
# ������ ������ �����: firm_1 ��� 10000 5000.
# ���������� ��������� ��������� ����, ��������� ������� ������
# ��������, � ����� ������� �������. ���� ����� �������� ������, � ������
# ������� ������� � �� ��������.����� ����������� ������. �� ������ ��������� ������� � ������� �
# �� ���������, � ����� ������� �� ������� ��������. ���� ����� ��������
# ������, ����� �������� � � ������� (�� ��������� �������).
# ������ ������: [{�firm_1�: 5000, �firm_2�: 3000, �firm_3�: 1000}, {�average_profit�: 2000}].
# �������� ������ ��������� � ���� json-������� � ���������������
# ����.
# ������ json-�������: [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit":2000}]
import json

# print(eval(input()))

firm_list = []

with open("files/laba1_task4.txt", "r") as file:
    for line in file:
        data = line.strip().split()
        name = data[0]
        ownership = data[1]  # ��������
        revenue = int(data[2])  # ������
        expenses = int(data[3])  # �������
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
