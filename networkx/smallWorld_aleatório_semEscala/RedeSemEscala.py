import networkx as nx
import matplotlib.pyplot as plt

def percorrer_dicionario(dicionario,n,m):
	eixoX=list()
	eixoY=list()

	for x in dicionario:
		eixoX.append(x)
		eixoY.append(dicionario[x])
		#print(x,dicionario[x])

	legenda="Para n=%d m=%d"%(n,m)
	plt.plot(eixoX, eixoY,label=legenda)
	plt.xlabel("Graus")
	plt.ylabel("Quantidade")
	plt.legend()


def CaminhoExiste(G,no1,no2):
	try:
		sp = nx.shortest_path(G,no1,no2)
	except nx.NetworkXNoPath:
		return False
	return True

def distancia(grafo):
	total=0
	contador=0
	SomaEfi=0
	for x in grafo:
		for y in grafo:
			if y!=x:
				if(CaminhoExiste(grafo,x,y)):
					#encontrar o caminho caminho mais curto entre um par de nós
					vetor=nx.dijkstra_path(grafo,x,y)
					soma=0.0
					for num in range(len(vetor)-1):
						numero1=vetor[num]
						numero2=vetor[num+1]
						#distancia do percurso
						soma=soma+1
				else:
					soma=1000000000000000000
				contador=contador+1
				#soma das eficiencias(cada par de nós possue apenas uma)
				SomaEfi=SomaEfi+(1/soma)
				#soma das distância
				total=total+soma
	dist=(total/contador)
	print("  Distancia média: %.2f"%dist)
	print("  Eficiencia média: %.2f"%(SomaEfi/contador))


def grafo_saida(grafo,n,m):
	#soma=0
	graus=dict()
	for x in grafo:
		arest=len(grafo[x])

		if (arest not in graus):
			graus[arest]=1
		else:
			graus[arest]=graus[arest]+1

		#print("Grau de saida do nó %d: %d"%(x,arest))
		#soma=soma+arest
	print("  Diâmetro: ",nx.diameter(grafo))
	percorrer_dicionario(graus,n,m) #dicionario com a frequência de cada grau

	#print("Quantidade de arestas:",soma/2)
	#print("Quantidade media de vizinhos: %.1f"%(soma/len(grafo)))

def densidade(n,grafo):
	max_aresta= (n*(n-1))/2
	soma=0
	for x in grafo:
		soma=soma+len(grafo[x])

	aresta_encontradas=soma/2

	if (max_aresta==0):
		print("Quantidade máxima de arestas: 0")
	else:
		densidade=aresta_encontradas/max_aresta
		print("Densidade encontrada: %.2f"%densidade)

#n=5
#m=4 #numero de arestas a serem adicionadas aleatoriamente a cada nó
p=0 #probabilidade de adionar um triângulo

'''for m in range(1,11):
	for n in range((m+1),11):
		grafo=nx.powerlaw_cluster_graph(n,m,p)
		print("n=%d m=%d"%(n,m))
		densidade(n,grafo)
		print("\n")'''


n=50
while(n<=200):
	for m in range(1,3):
		print("n=%d m=%d"%(n,m))
		grafo = nx.barabasi_albert_graph(n,m)
		grafo_saida(grafo,n,m)
		distancia(grafo)
	print("")
	n=n+50

#plt.grid(True)
#plt.show()

#grafo=nx.powerlaw_cluster_graph(10,5,p)
#grafo_saida(grafo)
