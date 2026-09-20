import sys

inicio = int(sys.argv[1])
fim = int(sys.argv[2])

for n in range(inicio, fim + 1):
    if n % 2 != 0:
        print(n)