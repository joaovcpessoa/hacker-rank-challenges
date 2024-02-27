# TAREFA: LISTAS
# Dado 3 números inteiros x,y e z representando as dimensões de um cubo junto com um número n.
# Imprima uma lista de todas as coordenadas possíveis dadas por (i,j,k) em uma grade 3D onde a soma de i + j + k não é igual a n. 
# Aqui, 0 <= i  <= x; 0 <= j  <= y; 0 <= k  <= z;
# Use compreensões de lista em vez de vários loops, como exercício de aprendizagem.
# Exemplo: x = 1; y = 1; z = 1; n = 3
# Saída:
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
# Restrições: Imprima a lista em ordem crescente lexicográfica

x = int(input('Digite o valor de x: '))
y = int(input('Digite o valor de y: '))
z = int(input('Digite o valor de z: '))
n = int(input('Digite o valor de n: '))

coordenadas = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if (i + j + k) != n]

print(f'Lista de novas coordenadas: {coordenadas}')

# Observações interessantes:

# coordenadas na verdade se torna uma matriz

# Primeiro loop (`for i in range(x + 1)'):
# range(x + 1) cria uma sequência de números de 0 a x (inclusive).
# i assume cada valor na sequência, representando a coordenada na dimensão x.

# Segundo loop (`for j in range(y + 1)'):
# range(y + 1) cria uma sequência de números de 0 a y (inclusive).
# j assume cada valor na sequência, representando a coordenada na dimensão y.

# Terceiro loop (`for k in range(z + 1)'):
# range(z + 1) cria uma sequência de números de 0 a z (inclusive).
# k assume cada valor na sequência, representando a coordenada na dimensão z.

# Condição (if (i + j + k) != n):
# Garante que apenas as combinações de coordenadas onde a soma de i, j e k não é igual a n serão incluídas na lista resultante.

# List Comprehension ([i, j, k]):
# Cria uma lista com as coordenadas [i, j, k] para cada combinação válida.