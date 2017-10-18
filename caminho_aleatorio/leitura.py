def lerArquivo(linhasIniciais,nos=None,arestas=None):
	Abrir = open('base_de_dados/ipv6.txt','r')
	NovoArquivo = open('base_de_dados/ipv6_TGF.txt','w')
	if nos is None:
		nos=list()
	if arestas is None:
		arestas=list()
	contador=1
	
	for linha in Abrir:
		if contador>linhasIniciais:
			vetor=linha.split() #quebrar linhas
			arestas.append(vetor) #adicionar arestas
			for x in vetor[0:2]:
				if x not in nos:
					NovoArquivo.writelines(x+"\n") #escrever cada número em uma linha
					nos.append(x)
		contador=contador+1
	NovoArquivo.writelines("#\n")
	for pares in arestas:
		NovoArquivo.writelines(pares[0]+" "+pares[1]+"\n")
	
lerArquivo(5375) #quantidade de linhas iniciais que devem ser ignoradas
#print(texto)
