'''
Celso Antonio Uliana Junior
September 2019
'''

n = int(input())

dic = {}

for i in range(n):
    row = list(map(str, input().split(' ')))
    key = row[1]
    if not key in dic:
        dic[key] = 1
    else:
        dic[key] += 1

for c in ('X', 'H', 'E', 'A', 'M'):
    if not c in dic:
        dic[c] = 0

print(str(dic['X']) + ' Hobbit(s)')
print(str(dic['H']) + ' Humano(s)')
print(str(dic['E']) + ' Elfo(s)')
print(str(dic['A']) + ' Anao(s)')
print(str(dic['M']) + ' Mago(s)')