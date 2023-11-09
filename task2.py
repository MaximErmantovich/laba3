# -*- coding: cp1251 -*-
# ������� ��������� ���� (�� ����������). ��������� ��������
# ������� ��������� � ������ �� 5 ��������� (�� ����� 10 �����). ���������
# ������� ���� ������� ��������. ������� �� ����� ���������, ��� �������
# ���� ���� 6.
# ������ �����:
# ������ 8 8 7 6 5
# ������ 5 6 7 7 6
def average_grade(text):
    summ = 0
    for i in range(1, 6):
        summ += int(text[i])
    return (summ / 5)


file = open('files/laba1_task2.txt', 'w')
print("������� ����� : ")
print('������ �����:\n������ 8 8 7 6 5\n������ 5 6 7 7 6')
print("��� ���������� ����� ������ ������ ������ � '����'")
list1 = []
while True:
    text = input()
    if text.lower() == '����' or text.lower() == 'stop':
        break
    if len(text.split()) != 6:
        print('������� ����� ������')
        continue
    file.write(text+'\n')
    text = text.split()
    if average_grade(text) < 6:
        list1.append(' '.join(text))
print('������� � ������� ������� ���� ���� 6')
for i in range(len(list1)):
    print(list1[i])
file.close()
