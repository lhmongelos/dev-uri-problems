'''
Celso Antonio
'''
n = m = 0
for i in range(100):
    a = int(input())
    if(a > m):
        m = a
        n = i + 1
print(m, n, sep='\n')