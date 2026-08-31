class No:
    def __init__(self, dado):
        # ALOCAÇÃO DINÂMICA: Ao instanciar um 'No', a memória é alocada 
        # dinamicamente no Heap do Python.
        self.dado = dado
        self.proximo = None

class ListaSimplesmenteEncadeada:
    def __init__(self):
        # Inicializa a lista vazia. A 'cabeca' aponta para None (nulo).
        self.cabeca = None

    def esta_vazia(self):
        """Verifica se a estrutura está vazia."""
        return self.cabeca is None

    def inserir(self, dado):
        """Insere um novo elemento no final da lista."""
        novo_no = No(dado) # Memória alocada dinamicamente para o novo nó
        
        if self.esta_vazia():
            self.cabeca = novo_no
        else:
            atual = self.cabeca
            while atual.proximo is not None:
                atual = atual.proximo
            # Encadeamento: a referência 'proximo' do último nó aponta para o novo nó
            atual.proximo = novo_no
        print(f"[{dado}] inserido com sucesso.")

    def exibir(self):
        """Percorre e exibe todos os elementos da lista."""
        if self.esta_vazia():
            print("A lista está vazia.")
            return

        atual = self.cabeca
        elementos = []
        while atual is not None:
            elementos.append(str(atual.dado))
            atual = atual.proximo
        print("Lista: " + " -> ".join(elementos) + " -> None")

    def buscar(self, dado):
        """Busca um elemento na lista e retorna se foi encontrado."""
        atual = self.cabeca
        posicao = 0
        while atual is not None:
            if atual.dado == dado:
                print(f"Busca: Elemento [{dado}] encontrado na posição {posicao}.")
                return True
            atual = atual.proximo
            posicao += 1
        print(f"Busca: Elemento [{dado}] não encontrado.")
        return False

    def remover(self, dado):
        """Remove a primeira ocorrência do elemento especificado."""
        if self.esta_vazia():
            print("Erro: Não é possível remover de uma lista vazia.")
            return

        # Caso 1: O elemento a ser removido é a cabeça da lista
        if self.cabeca.dado == dado:
            # GERENCIAMENTO DE MEMÓRIA:
            # Ao reatribuir self.cabeca, o nó original perde sua única referência ativa.
            # O contador de referências (Reference Counting) do Python cai para zero,
            # e a memória é liberada automaticamente pelo Garbage Collector.
            self.cabeca = self.cabeca.proximo
            print(f"Elemento [{dado}] removido do início.")
            return

        # Caso 2: O elemento está no meio ou no final
        atual = self.cabeca
        while atual.proximo is not None:
            if atual.proximo.dado == dado:
                # O nó que queremos remover é o 'atual.proximo'.
                # Para removê-lo, fazemos o nó 'atual' apontar para o nó seguinte a ele.
                # O nó removido fica sem referências e o Garbage Collector o limpa do Heap.
                atual.proximo = atual.proximo.proximo
                print(f"Elemento [{dado}] removido da lista.")
                return
            atual = atual.proximo
        
        print(f"Erro: Elemento [{dado}] não encontrado para remoção.")


# ==========================================
# PROGRAMA PRINCIPAL (TESTES E EVIDÊNCIAS)
# ==========================================
if __name__ == "__main__":
    print("--- INICIANDO TESTES DA LISTA ENCADEADA ---\n")
    lista = ListaSimplesmenteEncadeada()

    # 1. Tratamento de estrutura vazia
    lista.exibir()
    lista.remover(10)
    print("-" * 40)

    # 2. Inserção
    lista.inserir(10)
    lista.inserir(20)
    lista.inserir(30)
    lista.inserir(40)
    lista.exibir()
    print("-" * 40)

    # 3. Busca ou consulta
    lista.buscar(30)
    lista.buscar(99)
    print("-" * 40)

    # 4. Remoção
    # Removendo do meio
    lista.remover(20)
    lista.exibir()
    
    # Removendo do início
    lista.remover(10)
    lista.exibir()

    # Removendo do fim
    lista.remover(40)
    lista.exibir()
    
    print("\n--- FIM DOS TESTES ---")