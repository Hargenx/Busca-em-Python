def busca_binaria(base: list, nome: str) -> None:
    """
    Realiza uma busca binária na lista ordenada e imprime o resultado.

    Parameters:
    - base (list): A lista de nomes ordenada.
    - nome (str): O nome a ser buscado.
    """

    inicio = 0
    fim = len(base) - 1

    while inicio <= fim:
        metade = (inicio + fim) // 2

        if base[metade].lower() == nome:
            print(f'{nome.capitalize()} consta na lista de funcionários. Posição {metade}')
            break
        elif base[metade].lower() < nome:
            inicio = metade + 1
        else:
            fim = metade - 1
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

def main():
    lista_funcionarios = ['Clark', 'Peter', 'Bruce', 'Tony', 'Dianah',
                          'Natasha', 'Mari', 'Ororo', 'Raphael', 'Vivian']

    nome = input('Digite o nome a ser consultado: ').lower()

    if validar_entrada(nome, lista_funcionarios):
        busca_binaria(sorted(lista_funcionarios), nome)
    else:
        print('Nome inválido. Por favor, insira um nome válido da lista.')

if __name__ == "__main__":
    import time
    start = time.time()
    main()
    end = time.time()
    print(f'\nTempo total de execução: {end - start:.6f} segundos')
