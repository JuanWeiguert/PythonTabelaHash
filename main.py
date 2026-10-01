class Nodo:

    def __init__(self, sigla, nomeEstado):
        self.sigla = sigla
        self.nomeEstado = nomeEstado
        self.proximo = None

class ListaEncadeadaSimples:

    def __init__(self):
        self.head = None

    def inserir(self, sigla, nomeEstado):
        novo_nodo = Nodo(sigla, nomeEstado)
        novo_nodo.proximo = self.head
        self.head = novo_nodo

    def imprimir(self):
        nodo_atual = self.head

        while nodo_atual != None:
            print(nodo_atual.sigla, end=" -> ")
            nodo_atual = nodo_atual.proximo
        print("None")

class TabelaHash:

   def __init__(self):
       self.tam = 10
       self.h = [ListaEncadeadaSimples() for i in range(0, self.tam)]

   def inserir(self, sigla, nomeEstado):
       pos = self.hashFuncSigla(sigla, self.tam)
       self.h[pos].inserir(sigla, nomeEstado)

   def imprimir(self):
       for i in range(0, self.tam):
           print(i, end=": ")
           self.h[i].imprimir()


   def hashFuncSigla(self, k, n):
      if k == "DF":
          return 7

      return (ord(k[0]) + ord(k[1])) % n


tabela = TabelaHash()


tabela.inserir("AC", "Acre")
tabela.inserir("AL", "Alagoas")
tabela.inserir("AP", "Amapá")
tabela.inserir("AM", "Amazonas")
tabela.inserir("BA", "Bahia")
tabela.inserir("CE", "Ceará")
tabela.inserir("DF", "Distrito Federal")
tabela.inserir("ES", "Espírito Santo")
tabela.inserir("GO", "Goiás")
tabela.inserir("MA", "Maranhão")
tabela.inserir("MT", "Mato Grosso")
tabela.inserir("MS", "Mato Grosso do Sul")
tabela.inserir("MG", "Minas Gerais")
tabela.inserir("PA", "Pará")
tabela.inserir("PB", "Paraíba")
tabela.inserir("PR", "Paraná")
tabela.inserir("PE", "Pernambuco")
tabela.inserir("PI", "Piauí")
tabela.inserir("RJ", "Rio de Janeiro")
tabela.inserir("RN", "Rio Grande do Norte")
tabela.inserir("RS", "Rio Grande do Sul")
tabela.inserir("RO", "Rondônia")
tabela.inserir("RR", "Roraima")
tabela.inserir("SC", "Santa Catarina")
tabela.inserir("SP", "São Paulo")
tabela.inserir("SE", "Sergipe")
tabela.inserir("TO", "Tocantins")

tabela.inserir("JL", "Juan Weiguert de Lima")

tabela.imprimir()





