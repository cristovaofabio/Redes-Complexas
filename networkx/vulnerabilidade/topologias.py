import networkx as nx
import matplotlib.pyplot as plt

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
						soma=soma+grafo[numero1][numero2]['weight']
				else:
					soma=1000000000000000000
				contador=contador+1
				#soma das eficiencias(cada par de nós possue apenas uma)
				SomaEfi=SomaEfi+(1/soma)
				#soma das distância
				total=total+soma
	dist=(total/contador)
	nos=len(grafo)
	todasArestas=nos*(nos-1)/2 #todas as arestas possiveis
	#print("Distancia média: %.2f"%dist)
	print("Eficiencia: %.4f "%(SomaEfi/contador)) #mostro a média das eficiências
	Efici=(SomaEfi/contador)
	return Efici

def CaminhoExiste(G,no1,no2):
	try:
		sp = nx.shortest_path(G,no1,no2)
	except nx.NetworkXNoPath:
		return False
	return True

def criar_grafo_estrela(nos):
	grafo= nx.Graph() #nao direcionado
	grafo.add_node(nos)
	for x in range(nos):
		grafo.add_node(x)
		grafo.add_edge(nos,x,weight=1)
	return grafo

def criar_grafo_linear(nos):
	grafo= nx.Graph()
	antes=0
	grafo.add_node(antes)
	for x in range(1,(nos+1)):
		grafo.add_node(x)
		grafo.add_edge(antes,x,weight=1)
		antes=x
	return grafo


def criar_grafo_anel(nos):
	grafo= nx.Graph()
	antes=0
	grafo.add_node(antes)
	for x in range(1,(nos+1)):
		grafo.add_node(x)
		grafo.add_edge(antes,x,weight=1)
		antes=x
	grafo.add_edge(nos,0,weight=1)
	return grafo


def graficoLinha(x,y):
	plt.plot(x,y, label='Legenda da linha')
	plt.xlabel("Variavel x")
	plt.ylabel("Variavel y")
	plt.title("Teste Plot")
	plt.legend()
	plt.show()

def arestasRestantes(grafo):
	arestas=list() #guardar todas as arestas presentes
	for y in grafo:
		for x in grafo[y]:
			arestas.append([y,x])
	aRestantes=list()
	for y in grafo:
		for x in grafo:
			if (y!=x):
				if [y,x] not in arestas:
					aRestantes.append([y,x])
	return aRestantes

def adicionar_aresta(graf,aresta):
	graf.add_edge(aresta[0],aresta[1],weight=1)
	return graf

def arestas_presentes(grafo):
	arestas=list() #guardar todas as arestas presentes
	for y in grafo:
		for x in grafo[y]:
			arestas.append([y,x])
	return arestas

def remover_aresta(graf,aresta):
	graf.remove_edge(aresta[0],aresta[1])
	return graf

def maior_eficiencia(dicionario,eficiencia_inicial):
	maior=0.0;
	aresta=()
	for x in dicionario:
		if(dicionario[x]>maior):
			maior=dicionario[x]
			aresta=x

	print("Aresta de maior Eficiência: ",aresta, end="")
	print(" ----- %.4f"%maior)
	efi_ini=float(eficiencia_inicial)
	print("Vulnerabilidade: %.4f"%(efi_ini-maior))
		
	

def vulnerabilidade(Graf):
	#Existem duas estratégias para o cálculo de vulnerabiliadade:

	#Estratégia 1:  Isolando os nós por meio da remoção de duas arestas
	eficiencia_antes=distancia(Graf) #Eficiencia inicial
	for chave in Graf:
		arestas=list()
		nos=list()
		for valor in Graf[chave]:
			arestas.append([chave,valor])
			nos.append(valor)
		for no in nos:
			Graf=remover_aresta(Graf,[chave,no])
		print("Remoção das arestas do nó: %d "%chave)
		eficiencia_depois=distancia(Graf) #eficiencia depois de remover as arestas
		print("Vulnerabilidade: %.4f "%((eficiencia_antes-eficiencia_depois)/eficiencia_antes))
		print("")
		for vetor in arestas:
			Graf=adicionar_aresta(Graf,vetor)

	#Estratégia 2:  Removendo os nós do grafo	
	'''eficiencia_antes=distancia(Graf) #Eficiencia inicial
	estado=dict()
	for x in Graf:
		estado=Graf[x]
		no=x
		Graf.remove_node(x)
		print("")
		print("Remoção apenas do nó: %d "%x)
		eficiencia_depois=distancia(Graf)
		print("Vulnerabilidade: %.4f "%((eficiencia_antes-eficiencia_depois)/eficiencia_antes))
		Graf.add_node(no)
		for y in estado:
			Graf.add_edge(no,y,weight=1)'''


quant_nos=13 #quantidade de nós no meu grafo
grafo = criar_grafo_linear(quant_nos-1)
vulnerabilidade(grafo)

'''arestas_restantes=arestasRestantes(grafo)
eficiencia_inicial=distancia(grafo)


dic_eficiencias=dict()

for x in arestas_restantes:
	grafo=adicionar_aresta(grafo,x)
	print("Aresta: ",x, end="")
	num1=x[0]
	num2=x[1]
	dic_eficiencias[(num1,num2)]=distancia(grafo) #guarda a eficiência de cada aresta
	grafo=remover_aresta(grafo,x)

maior_eficiencia(dic_eficiencias,eficiencia_inicial)'''


	
#graficoLinha(x,y)