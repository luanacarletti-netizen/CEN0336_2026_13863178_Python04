numbers = [101, 2, 15, 22, 95, 33, 2, 27, 72, 15, 52]

numbers = sorted(numbers)

soma_pares = 0
soma_impares = 0

for n in numbers:
    print(n)

    if n % 2 == 0:
        soma_pares += n
    else:
        soma_impares += n

print("Soma dos números pares:", soma_pares)
print("Soma dos números ímpares:", soma_impares)