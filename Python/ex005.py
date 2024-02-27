# TAREFA: Loop For
# Dado um número n. Sem usar nenhum método de string, tente imprimir o seguinte:
# Exemplo: n = 5
# Saída:
# 1 2 3 4 5
# Imprima a sequência
# Restrições: 1 <= n <= 150

n = int(input('Digite o número: '))

sequence = []

if 1 <= n <= 150:
    sequence = list(range(1, n + 1))
    print(*sequence, sep=' ')
else:
    print('Por favor, digite um número entre 1 e 150.')