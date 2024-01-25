class BinaryTreeNode:
    def __init__(self, nome: str) -> None:
        """
        Inicializa um nó da árvore de pesquisa binária.

        Parameters:
        - nome (str): O nome associado ao nó.
        """
        self.nome = nome
        self.esq = self.dir = None

def insere_na_arvore_binaria(raiz: BinaryTreeNode, nome: str) -> BinaryTreeNode:
    """
    Insere um novo nó na árvore de pesquisa binária.

    Parameters:
    - raiz (BinaryTreeNode): A raiz da árvore.
    - nome (str): O nome a ser inserido na árvore.

    Returns:
    - BinaryTreeNode: A raiz da árvore após a inserção.
    """
    if raiz is None:
        return BinaryTreeNode(nome)
    
    if nome < raiz.nome:
        raiz.esq = insere_na_arvore_binaria(raiz.esq, nome)
    elif nome > raiz.nome:
        raiz.dir = insere_na_arvore_binaria(raiz.dir, nome)
    
    return raiz

def construir_arvore_binaria(base: list) -> BinaryTreeNode:
    """
    Constrói uma árvore de pesquisa binária a partir de uma lista de nomes.

    Parameters:
    - base (list): A lista de nomes.

    Returns:
    - BinaryTreeNode: A raiz da árvore de pesquisa binária.
    """
    raiz = None

    for nome in map(str.lower, base):
        raiz = insere_na_arvore_binaria(raiz, nome)

    return raiz

def busca_na_arvore_binaria(raiz: BinaryTreeNode, nome: str, base: list) -> None:
    """
    Realiza uma busca na árvore de pesquisa binária e imprime o resultado.

    Parameters:
    - raiz (BinaryTreeNode): A raiz da árvore de pesquisa binária.
    - nome (str): O nome a ser buscado.
    - base (list): A lista original de nomes.
    """

    resultado = busca_arvore_binaria(raiz, nome)

    if resultado:
        indice = base.index(resultado.nome.capitalize())
        print(f'{nome.capitalize()} consta na lista de funcionários. Posição {indice}')
    else:
        print(f'{nome.capitalize()} não consta na lista de funcionários.')
def busca_arvore_binaria(raiz: BinaryTreeNode, nome: str) -> BinaryTreeNode:
    
    """
    Busca um nó na árvore de pesquisa binária.

    Parameters:
    - raiz (BinaryTreeNode): A raiz da árvore de pesquisa binária.
    - nome (str): O nome a ser buscado na árvore.

    Returns:
    - BinaryTreeNode: O nó encontrado ou None se não encontrado.
    """
    
    while raiz is not None and raiz.nome != nome:
        raiz = raiz.esq if nome < raiz.nome else raiz.dir
    
    return raiz

def validar_entrada(nome: str, base: list) -> bool:
    """
    Valida se o nome inserido pelo usuário está na lista.

    Parameters:
    - nome (str): O nome a ser validado.
    - base (list): A lista original de nomes.

    Returns:
    - bool: True se o nome for válido, False caso contrário.
    """
    return nome.lower() in map(str.lower, base)

# Exemplo de uso
def main():
    lista_funcionarios = ['Clark', 'Peter', 'Bruce', 'Tony', 'Dianah',
                          'Natasha', 'Mari', 'Ororo', 'Raphael', 'Vivian']

    nome = input('Digite o nome a ser consultado: ').lower()

    if validar_entrada(nome, lista_funcionarios):
        # Utilizando árvore de pesquisa binária
        raiz_binaria = construir_arvore_binaria(lista_funcionarios)
        busca_na_arvore_binaria(raiz_binaria, nome, lista_funcionarios)

        # Utilizando árvore genérica (descomente se necessário)
        # raiz_generica = construir_arvore(lista_funcionarios)
        # busca_na_arvore(raiz_generica, nome, lista_funcionarios)
    else:
        print('Nome inválido. Por favor, insira um nome válido da lista.')

if __name__ == "__main__":
    import time
    start = time.time()
    main()
    end = time.time()
    print(f'\nTempo total de execução: {end - start:.6f} segundos')
