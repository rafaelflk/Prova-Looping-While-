
soma = 0
qtdNumeros = 0

while True:
    numero = int(input('Digite um número inteiro. "zero (0) para sair".: '))
    
    if numero == 0:
        break

    soma += numero
    qtdNumeros += 1

media = soma / qtdNumeros

print('Qauntidade de números digitados foi: ', qtdNumeros)
print('A soma dos números digitados é: ', soma)
print('A média dos números digitados é: ', media)
