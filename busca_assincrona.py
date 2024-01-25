import asyncio

async def busca(base: list, nome: str, inicio: int, fim: int) -> int:
    """
    Realiza uma busca binária assíncrona na lista ordenada.

    Parameters:
    - base (list): A lista de nomes ordenada.
    - nome (str): O nome a ser buscado.
    - inicio (int): Índice inicial da busca.
    - fim (int): Índice final da busca.

    Returns:
    - int: A posição do nome na lista ou -1 se não encontrado.
    """
    while inicio <= fim:
        metade = (inicio + fim) // 2

        if base[metade].lower() == nome:
            return metade
        elif base[metade].lower() < nome:
            inicio = metade + 1
        else:
            fim = metade - 1

    return -1

async def busca_assincrona(base: list, nome: str) -> int:
    """
    Realiza uma busca binária assíncrona na lista ordenada.

    Parameters:
    - base (list): A lista de nomes ordenada.
    - nome (str): O nome a ser buscado.

    Returns:
    - int: A posição do nome na lista ou -1 se não encontrado.
    """
    return await busca(base, nome, 0, len(base) - 1)

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

async def main():
    lista_funcionarios = ['Clark', 'Peter', 'Bruce', 'Tony', 'Dianah',
                          'Natasha', 'Mari', 'Ororo', 'Raphael', 'Vivian']

    nome = input('Digite o nome a ser consultado: ').lower()

    if validar_entrada(nome, lista_funcionarios):
        resultado = await busca_assincrona(sorted(lista_funcionarios), nome)
        if resultado != -1:
            print(f'{nome.capitalize()} consta na lista de funcionários. Posição {resultado}')
        else:
            print(f'{nome.capitalize()} não consta na lista de funcionários.')
    else:
        print('Nome inválido. Por favor, insira um nome válido da lista.')

if __name__ == "__main__":
    import time
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'\nTempo total de execução: {end - start:.6f} segundos')
