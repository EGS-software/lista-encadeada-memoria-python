# Lista Encadeada com Gerenciamento de Memória em Python

Este projeto implementa uma **Lista Simplesmente Encadeada** em Python, demonstrando os conceitos fundamentais de alocação dinâmica de memória, encadeamento de nós e gerenciamento automático de memória através do Garbage Collector do Python.

## 📋 Conteúdo

- **`lista_encadeada.py`**: Implementação completa da estrutura de dados com operações de inserção, remoção, busca e exibição
- **`tests/`**: Testes da implementação
- **`img/`**: Imagens e recursos visuais

## 🎯 Funcionalidades

- ✅ Inserção de elementos no final da lista
- ✅ Remoção de elementos (início, meio ou fim)
- ✅ Busca de elementos
- ✅ Exibição da estrutura
- ✅ Verificação de lista vazia

## 🔧 Conceitos Implementados

### Alocação Dinâmica
Cada novo nó é alocado dinamicamente no Heap durante a execução do programa.

### Encadeamento
Os nós são conectados através de referências (ponteiros), formando uma cadeia linear.

### Gerenciamento de Memória
O Python utiliza **Reference Counting** e **Garbage Collector** para liberar automaticamente a memória de nós que não possuem mais referências.

## 📝 Uso

```python
from lista_encadeada import ListaSimplesmenteEncadeada

lista = ListaSimplesmenteEncadeada()
lista.inserir(10)
lista.inserir(20)
lista.exibir()
lista.buscar(10)
lista.remover(10)
```

## 👤 Autor

Criado por [jvbenetti](https://github.com/jvbenetti)

## 📄 Licença

Este projeto é fornecido como material educacional.
