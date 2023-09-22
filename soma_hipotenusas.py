def é_hipotenusa(n):
    for i in range(1, n):
        for j in range(i, n):
            if n ** 2 == i ** 2 + j ** 2:
                return True
    return False

def soma_hipotenusas(n):
    soma = 0
    for num in range(1, n + 1):
        if é_hipotenusa(num):
            soma += num
    return soma