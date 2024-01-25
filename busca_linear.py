def busca_linear(base: list, nome: str) -> None:
    """
    Realiza uma busca linear na lista e imprime o resultado.

    Parameters:
    - base (list): A lista de nomes.
    - nome (str): O nome a ser buscado.
    """

    for i, item in enumerate(map(str.lower, base)):
        if item == nome:
            print(f'{nome.capitalize()} consta na lista de funcionários. Posição {i}')
            break
    else:
        print(f'{nome.capitalize()} não consta na lista de funcionários.')

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

# Restante do código permanece o mesmo


def main():
    lista_funcionarios = ['Clark', 'Peter', 'Bruce', 'Tony', 'Dianah',
                          'Natasha', 'Mari', 'Ororo', 'Raphael', 'Vivian']

    nome = input('Digite o nome a ser consultado: ').lower()

    if validar_entrada(nome, lista_funcionarios):
        busca_linear(lista_funcionarios, nome)
    else:
        print('Nome inválido. Por favor, insira um nome válido da lista.')

if __name__ == "__main__":
    import time
    start = time.time()
    main()
    end = time.time()
    print(f'\nTempo total de execução: {end - start:.6f} segundos')