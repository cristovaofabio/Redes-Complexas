#dic = {'A':['B','C'],'B':['A','C','D'],'C':['A','B','D'],'D':['B','C']}
#Abaixo se encontra uma grafo não direcionado sem peso
dic = { 1:[2,3,4], 2:[1,3],3:[2,1],4:[1]}
#Obervação: caso tenha pesos nas arestas, crie uma matriz para guardar os valores


import networkx as nx

def criar_matriz(tamanho):
	matriz=[]
	for i in range(tamanho):
		linha = []
		for j in range(tamanho):
			 linha.append(0)
		matriz.append(linha)

def caminho(v1,v2):
	for chave in  dic:
		encontrar=0
		if(chave==v1):
			for x in dic[chave]:
				if(x==v2):
					print("Caminho existente")
					encontrar=1
			if (encontrar==0):
				print("Caminho não existente")

def gerarDict(dic=None,arestas=None,nos=None):
	#nesta função estou gerando uma lista adjacente de saida
	if dic is None:
		dic=dict()
	if arestas is None:
		arestas=list()
	if nos is None:
		nos=list()
	marcador=0
	Abrir = open('ipv6_TGF.txt','r')
	for linha in Abrir:
		vetor=linha.split() #quebrar linhas
		if(vetor[0]=="#"):
			marcador=1
		if (marcador!=1):
			numero=int(vetor[0])
			if numero not in nos:
				nos.append(numero)
			if numero not in dic:
				dic[numero]=[]
		if (marcador==1 and vetor[0]!="#"):
			arestas.append(vetor)
			no1=int(vetor[0])
			no2=int(vetor[1])
			if no2 not in dic[no1]:
				dic[no1].append(no2)
			if no1 not in dic[no2]:
				dic[no2].append(no1)
			
	quant_arest=int(len(arestas))
	print("Quantidade de arestas:",quant_arest)
	return dic
	#print(dic)

def percorrerRota(v1,v2,possibilidades=None):
	if possibilidades is None:
		possibilidades=[]
	#possibilidades.append(v1) #usado para mostrar apenas uma rota 
	possibilidades=possibilidades+[v1] #usado para mostrar todas as rotas
	if v1==v2:
		return possibilidades
	for valor in dic[v1]:
		if valor not in possibilidades:
			rota=percorrerRota(valor,v2,possibilidades)
			if (rota):
				casos.append(rota)
				print(rota)
	return None

def menor_distancia(casos,dic):
	menor=list()
	if casos!=[]:
		menor=casos[0]
		for i in casos:
			if len(i)<len(menor):
				menor=i
	
	return menor

def maior_distancia(casos,dic):
	maior=list()
	if casos!=[]:
		maior=casos[0]
		for i in casos:
			if len(i)>len(maior):
				maior=i
	
	return maior

def distancias(casos,dic):
	somaCaminhos=0
	for i in range(len(casos)):
		soma=0
		for j in range(len(casos[i])-1):
			pri = casos[i][j]
			seg = casos[i][j+1]
			soma=soma+dic[pri][seg]
		somaCaminhos=somaCaminhos+soma
	print("soma: ",soma)
	return somaCaminhos

def densidade(dic):
	aresta=0
	for chave in dic:
		aresta=aresta+len(dic[chave])
	aresta=aresta/2 #se não for direcionado
	quantNos=len(dic)
	#quantMaxima=quantNos*(quantNos-1) #se for direcionado
	quantMaxima=quantNos*(quantNos-1)/2 #se não for direcionado
	print("Densidade: %.2f"%(aresta/quantMaxima))

def probabilidade(dic):
	graus=dict()
	for chave in dic:
		gr=len(dic[chave])
		if gr not in graus:
			graus[gr]=1
		else:
			quant=graus[gr]+1
			graus[gr]=quant

	for chave in graus:
		prob=graus[chave]/len(dic)
		print("Probabilidade de econtrar um nó com grau %d: %.2f"%(chave,prob))

dic=gerarDict()
soma=0
somaM=0
contador=0
contadorM=0
for chave1 in dic:
	for chave2 in dic:
		if(chave1!=chave2):
			casos=[]
			percorrerRota(chave1,chave2)
			result=menor_distancia(casos,dic)#apenas as menores distâncias
			resultM=maior_distancia(casos,dic)#apenas as maiores distâncias
			if result!=[]:
				contador=contador+1
				soma=soma+(len(result)-1) #quant arestas menor caminho
			if resultM!=[]:
				contadorM=contadorM+1
				somaM=somaM+(len(resultM)-1)

tamanho=(len(dic))
tamanho=tamanho*(tamanho-1)/2

efi=1/(soma/contador)
print("Distância média: %.2f"%(soma/contador))
print("Diâmetro: %.2f"%(somaM/contadorM))
print("Eficiencia: %.2f"%efi)
densidade(dic)
#probabilidade(dic,2)
'''casos=[]
percorrerRota("A","F")
print("Todas as rotas: ",casos)
maior_distancia(casos,dic)'''