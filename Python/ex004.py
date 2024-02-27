# TAREFA: LOOP FOR
# Dado um número n. Para todos os inteiros não negativos i < n, imprimir i^2
# Restrições: 1 <= n <= 20 
# Exemplo: n = 5
# Saída:
# 0 
# 1 
# 4 
# 9 
# 16

n = int(input('Digite o número: '))

if 1 <= n <= 20:
    for i in range(n):
        print(i**2)
else:
    print('Por favor, digite um número entre 1 e 20.')