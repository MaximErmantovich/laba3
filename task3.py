# -*- coding: cp1251 -*-
# ������������ (�� ����������) ��������� ����. � �� ������
# ������ ������ ��������� ������� ������� � ������� ����������,
# ������������ � ������������ ������� �� ��������. ���� ������ ������� �
# ���������� �������. �������������, ����� ��� ������� �������� ���� ���
# ���� �������.
# ������������ �������, ���������� �������� �������� � �����
# ���������� ������� �� ����. ������� ��� �� �����.
# ������� ����� �����:
# �����������: 100(�) 50(��) 20(���).
# ������: 30(�) 10(���)
# �����������: 30(��)

file = open('files/laba1_task3.txt', 'w')
dictionary = {'�����������': 0, '������': 0,
              '�����������': 2, "����������": 0, '�������': 0, '����������': 0}
print("��� ���������� ����� ������ ������ ������ � '����'")
while True:
    print('������� ������������ �������:')
    name = input()
    if name in dictionary.keys():
        while True:
            lk = int(input('������� ������� ����� (��) '))
            pz = int(input('������� ������� ����� (��) '))
            lab = int(input('������� ������� ����� (���) '))
            if lab + pz + lk == dictionary[f'{name}']:
                if lab == 0:
                    if pz == 0:
                        file.write(f'{name}: {lk}(�)' + '\n')
                    elif lk == 0:
                        file.write(f'{name}: {pz}(��) ' + '\n')
                    else:
                        file.write(f'{name}: {lk}(�) {pz}(��)' + '\n')
                elif pz == 0:
                    if lk == 0:
                        file.write(f'{name}: {lab}(���)' + '\n')
                    else:
                        file.write(f'{name}: {lk}(�) {lab}(���)' + '\n')
                elif lk == 0:
                    file.write(f'{name}: {pz}(��) {lab}(���)' + '\n')
                else:
                    file.write(f'{name}: {lk}(�) {pz}(��) {lab}(���)'+'\n')
                break
            else:
                print('������� ��������� ���������� �����')
    else:
        if name.lower() == '����' or name.lower() == 'stop':
            break
        else:
            print('������� ������������ ������� ���������')
file.close()
with open("files/laba1_task3.txt", "r") as file:
    for line in file:
        data = line.strip().split()
