'''
------------------------UNIVERSIDADE FEDERAL DO SUL E SUDESTE DO PARÁ--------------------------
COMPLEXIDADE DE ALGORITMOS                  ALGORITMO DE KRUSKAL - Árvore Geradora Mínima                 
Algoritmo Guloso
Professor: Manoel Ribeiro 

Discentes:
1. Amanda Fiel Savino
2. Beatriz de Jesus Silva Cavalcante 
3. Manoel Malon Costa de Moura
'''

import heapq

#ler o número de vertices e arestas
nomeArquivo = input("Digite o nome de algum dos exemplos txt do diretório ou crie o seu e importe (obs: não esqueça de digitar .txt): ")

#abrir o arquivo txt especificado
arquivo = open(nomeArquivo, 'r')
conteudo = arquivo.read()

#pegar o valor de vertices (1ª palavra)
n = conteudo.split()[0]

#pegar o valor de arestas (2ª palavra)
m = conteudo.split()[1]

n = int(n)
m = int(m)

H = []
#ler as m arestas do digrafo
for j in range(2, m*3, 3):

    a = conteudo.split()[j]
    b = conteudo.split()[j+1]
    custo = conteudo.split()[j+2]

    a = int(a)
    b = int(b)
    custo = int(custo)
    
    heapq.heappush(H, (custo, a, b))    #colocar aresta no heap

#criar n conjuntos
conjunto = [[]*n for i in range(n)]

for i in range(n):
    conjunto[i].append(i)      #cada C[i] é inicializado com (i)

S = []
for i in range(n):
    S.append(i)     #S[i] é o conjunto ao qual o vértice i pertence

print("\nConjunto e hash dos vertices originais: ")
print(conjunto)
print(S, "\n-----------------------------------------------------------------")

cont = 0
custoTotal = 0

while cont < n-1:   #bastam n-1 arestas
    custo, a, b = heapq.heappop(H)  #remover a próxima aresta do heap
    if S[a] != S[b]:    #se as arestas unem arvóres diferentes
        custoTotal = custoTotal + custo
        p = S[a]
        q = S[b]
        if q < p:
            p, q = q, p
        for j in conjunto[q]:  #para cada j no conjunto C[q]
            S[j] = p
        conjunto[p].extend(conjunto[q])   #unir C[p] e C[q] (a união fica em C[p])
        conjunto[q] = []     #esvaziar C[q]
        cont = cont + 1
        print("Passo ", cont, ":")
        print("Conjunto: ", conjunto)
        print("Hash dos vertices: ", S, "\n")
print("A soma das arestas da árvore geradores mínima é: ", custoTotal)

