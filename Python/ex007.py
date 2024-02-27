# TAREFA: Descubra a pontuação do vice-campeão.
# Dada a planilha de pontuação dos participantes para o Dia do Esporte Universitário, 
# você deverá encontrar a pontuação do segundo colocado. 
# Você recebe pontuações. Armazene-os em uma lista e descubra a pontuação do vice-campeão.
# Exemplo: n = 5, arr = 2 3 6 6 5
# Saída:
# 5
# Restrições: 2 <= n < 10; -100 <= A[i] <= 100
n = int(input('Digite o valor de n: '))
a = map(int, input('Digite a matriz dos resultados:').split())
a = list(set(a))
a.remove(max(a))
print(max(a))