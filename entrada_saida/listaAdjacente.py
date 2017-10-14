import time
import matplotlib.pyplot as plt
from pylab import *

def histograma(idades,bins):
	plt.hist(idades,bins,histtype='bar', rwidth=1)
	plt.show()

def gerarDict(dic=None,arestas=None,nos=None):
	#nesta função estou gerando uma lista adjacente de saida
	if dic is None:
		dic=dict()
	if arestas is None:
		arestas=list()
	if nos is None:
		nos=list()
	marcador=0
	Abrir = open('grafoNetworkTGF.txt','r')
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
	quant_nos=int(len(nos))
	quant_arest=int(len(arestas))
	print("Quantidade de arestas:",quant_arest)
	max_arest=quant_nos*(quant_nos-1)#calculo para grafos direcionados
	print("Densidade: %.2f"%(quant_arest/max_arest))
	return dic
	#print(dic)

def procurar_nao_ralos(grafo): #não ralo = possui saidas
	possiveis_nao_ralos=dict()
	for x in grafo:
		arest=len(grafo[x]) #quantidade de saidas para um determinado nó
		if x not in possiveis_nao_ralos:
			if arest!=0:
				possiveis_nao_ralos[x]=[arest]
	return possiveis_nao_ralos

def procurar_ralos(grafo): #ralo = tem entradas, mas não possui saidas
	possiveis_ralos=list()
	for x in grafo:
		arest=len(grafo[x]) #quantidade de saidas para um determinado nó
		if x not in possiveis_ralos:
			if arest==0: #se um determinado nó não tiver saida
				possiveis_ralos.append(x)
	return possiveis_ralos

def histograma_grafo(grafo):
	#bins = [0,1,2,3,4,5,6,7,8,9,10] #intervalos, neste caso é apenas um exemplo
	valores=list()
	bins=list() #intervalos
	for x in grafo:
		arest=len(grafo[x])
		valores.append(arest)
	valorMax=max(valores)+1
	for h in range(valorMax):
		bins.append(h)
	histograma(valores,bins)

def grafo_saida(grafo):
	soma=0
	for x in grafo:
		arest=len(grafo[x])
		print("Grau de saida do nó %d: %d"%(x,arest))
		soma=soma+arest
	print("Quantidade de visinhos:",soma)
	print("Quantidade media de vizinhos: %.1f"%(soma/len(grafo)))
	print("Quantidade esperada de visinhos:",(len(grafo)-1))#para um grafo direcionado
	histograma_grafo(grafo)
	
def grafo_entrada(grafo):
	#para gerar grafo de entrada
	entrada=dict()
	naoRalos=procurar_nao_ralos(grafo) #possuem saidas
	ralos=procurar_ralos(grafo) # não possuem saidas
	for x in grafo:
		entrada[x]=[]
	for y in grafo:
		for g in grafo[y]:
			if(g in entrada):
				entrada[g].append(y)

	#para verificar quem possui apenas saidas
	for x in entrada:
		arest=len(entrada[x]) #quantidadade de entradas no nó
		#print("Grau de entrada do nó %d: %d"%(x,arest))
		if (arest==0):
			if x in naoRalos:
				print("Possuem apenas saidas: ",x,naoRalos[x])
		#if(arest!=0):
		#	if x in ralos:
		#		print("Ralos: ",x)
	
	histograma_grafo(entrada)
	#return entrada
	
def procurar_aresta(grafo):
	arquivo = open('nos','r')
	for linha in arquivo:
		vetor=linha.split()
		num1=int(vetor[0])
		num2=int(vetor[1])
		inicio=time.time()
		for x in grafo:
			if x==num1:
				for y in grafo[x]:
					if y==num2:
						break
				break
		fim=time.time()
		print("Tempo:",(fim-inicio))

Grafo=gerarDict()
#procurar_aresta(Grafo)
#grafo_saida(Grafo)
#entrada=grafo_entrada(Grafo)
grafo_saida(Grafo)