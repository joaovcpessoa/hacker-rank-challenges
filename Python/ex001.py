# TAREFA: IF ELSE
# Dado um número inteiro,, execute as seguintes ações condicionais:
# Se n é ímpar, imprima "Ímpar"
# Se n é par e está na faixa entre 2 e 5 , imprimir "Par e dentro da primeira faixa"
# Se n é par e está na faixa entre 6 e 20, imprimir "Par e dentro da segunda faixa"
# Se é par e maior que 20, imprimir "Par e maior que 20"
# Exemplo: n = 5
# Saída: 
# Restrições: 1 <= n <= 100

n = int(input("Digite o numero: ").strip())

if 1 <= n <= 100:
    if n % 2 == 0:
        if 2 <= n <= 5:
            print("Par e dentro da primeira faixa")
        elif 6 <= n <= 20:
            print("Par e dentro da segunda faixa")
        elif 6 <= n <= 20:
            print("Par e dentro da segunda faixa")
    else:
        print("Impar")
else:
    print('Por favor, digite um número entre 1 e 100.')