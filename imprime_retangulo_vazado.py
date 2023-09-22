largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

for i in range(altura):
    if i == 0 or i == altura - 1:
        # Se for a primeira ou última linha, imprime uma linha completa de '#'
        print('#' * largura)
    else:
        # Se não for a primeira ou última linha, imprime bordas '#' no início e fim,
        # e espaços em branco no meio
        print('#' + ' ' * (largura - 2) + '#')
