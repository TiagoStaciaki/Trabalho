from .Arquivos.adicionar import lerPokedex, atualizarHP
from .listarPokemons import listarPokemons
from time import sleep
vida = True

def batalha():
    global vida
    dadosPokemons = lerPokedex()

    print('Deseja listar o pokemons disponiveis?')
    print('1 - Sim')
    print('2 - Não')
    opcao = int(input('Digite aqui: '))

    match opcao:
        case 1:
            listarPokemons()
            pPokemon, sPokemon = selecionar(dadosPokemons)

        case 2:
            pPokemon, sPokemon = selecionar(dadosPokemons)

    while True:
        if pPokemon['Iniciativa'] > sPokemon['Iniciativa']:
            print(f'A batalha começa!')
            sleep(3)
            while True:
                apPokemon(pPokemon, sPokemon)
                if vida == False:
                    break
                asPokemon(sPokemon, pPokemon)
            break

        elif sPokemon['Iniciativa'] > pPokemon['Iniciativa']:
            print(f'A batalha começa!')
            sleep(3)
            while True:
                asPokemon(sPokemon, pPokemon)
                if vida == False:
                    break
                apPokemon(pPokemon, sPokemon)
            break

def apPokemon(pPokemon, sPokemon):
    vindo = 'Batalha'
    global vida
    print(f'Vez de {pPokemon["Nome"]}')
    print('Ataques disponiveis: ')
    print(f'{pPokemon["Nome do ataque 1"]:<25} {pPokemon["Nome do ataque 2"]}')

    opcao = input('Digite o aqui: ')
    
    if opcao == pPokemon['Nome do ataque 1']:
        print(f'{sPokemon["Nome"]} sofreu {pPokemon["Valor do ataque 1"]} de dano')
        sPokemon['HP atual'] = int(sPokemon['HP atual']) - int(pPokemon['Valor do ataque 1'])
        atualizarHP(sPokemon, vindo)

        if int(sPokemon['HP atual']) <= 0:
            print(f'{sPokemon["Nome"]} foi derrotado')
            print(f'{pPokemon["Nome"]} venceu!')
            vida = False
        
        else:
            vida = True

    elif opcao == pPokemon['Nome do ataque 2']:
        print(f'{pPokemon["Nome"]} sofreu {sPokemon["Valor do ataque 2"]} de dano')
        sPokemon['HP atual'] = int(sPokemon['HP atual']) - int(pPokemon['Valor do ataque 2'])
        atualizarHP(sPokemon, vindo)

        if int(pPokemon['HP atual']) <= 0:
            print(f'{pPokemon["Nome"]} foi derrotado')
            print(f'{sPokemon["Nome"]} venceu!')
            vida = False
        
        else:
            vida = True

def asPokemon(sPokemon, pPokemon):
    vindo = 'batalha'
    global vida
    print(f'Vez de {sPokemon["Nome"]}')
    print('Ataques disponiveis: ')
    print(f'{sPokemon["Nome do ataque 1"]:<25} {sPokemon["Nome do ataque 2"]}')

    opcao = input('Digite o nome do ataque: ')
    
    if sPokemon['Nome do ataque 1'] == opcao:
        print(f'{pPokemon["Nome"]} sofreu {sPokemon["Valor do ataque 1"]} de dano')
        pPokemon['HP atual'] = int(pPokemon['HP atual']) - int(sPokemon['Valor do ataque 1'])
        atualizarHP(pPokemon, vindo)

        if int(pPokemon['HP atual']) <= 0:
            print(f'{pPokemon["Nome"]} foi derrotado')
            print(f'{sPokemon["Nome"]} venceu!')
            vida = False
        
        else:
            vida = True
    
    elif sPokemon['Nome do ataque 2'] == opcao:
        print(f'{pPokemon["Nome"]} sofreu {sPokemon["Valor do ataque 2"]} de dano')
        pPokemon['HP atual'] = int(pPokemon['HP atual']) - int(sPokemon['Valor do ataque 2'])
        atualizarHP(pPokemon, vindo)

        if int(pPokemon['HP atual']) <= 0:
            print(f'{pPokemon["Nome"]} foi derrotado')
            print(f'{sPokemon["Nome"]} venceu!')
            vida = False
        
        else:
            vida = True

def selecionar(dadosPokemons):
    pCodigo = int(input('Digite o código do primeiro pokemon desejado: '))
    sCodigo = int(input('Digite o código do segundo pokemon desejado: '))

    for pokemon in dadosPokemons:
        if int(pokemon['Número Pokedex']) == pCodigo:
            pPokemon = pokemon

        elif int(pokemon['Número Pokedex']) == sCodigo:
            sPokemon = pokemon

    return pPokemon, sPokemon