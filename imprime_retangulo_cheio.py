largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

linha = '#' * largura  # Cria uma linha com '#' repetidos largura vezes

for i in range(altura):
    print(linha, end='')
    if i < altura - 1:
        print()  # Pula para a próxima linha (exceto na última linha)
