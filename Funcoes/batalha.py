from .Arquivos.adicionar import lerPokedex, atualizarHP
from .listarPokemons import listarPokemons
from time import sleep
from random import randint

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

    if int(pPokemon['HP atual']) == 0 or int(sPokemon['HP atual']) == 0:
        if int(pPokemon['HP atual']) == 0:
            print(f'{pPokemon["Nome"]} está incapacitado para lutar!')
        
        if int(sPokemon['HP atual']) == 0:
            print(f'{sPokemon["Nome"]} está incapacitado para lutar!')
    else: 
        while vida:
            if int(pPokemon['Iniciativa']) > int(sPokemon['Iniciativa']):
                print(f'A batalha começa!')
                sleep(3)
                while True:
                    apPokemon(pPokemon, sPokemon)
                    if vida == False:
                        break
                    asPokemon(sPokemon, pPokemon)
                    if vida == False:
                        break
                break

            elif int(sPokemon['Iniciativa']) > int(pPokemon['Iniciativa']):
                print(f'A batalha começa!')
                sleep(3)
                while True:
                    asPokemon(sPokemon, pPokemon)
                    if vida == False:
                        break
                    apPokemon(pPokemon, sPokemon)
                    if vida == False:
                        break
                break

            elif pPokemon['Iniciativa'] == sPokemon['Iniciativa']:
                aleatorio = randint(1, 2)
                if aleatorio == 1:
                    pPokemon['Iniciativa'] = int(pPokemon['Iniciativa']) + 1
                    continue

                elif aleatorio == 2:
                    sPokemon['Iniciativa'] = int(pPokemon['Iniciativa']) + 1
                    continue

        vida = True

def apPokemon(pPokemon, sPokemon):
    vindo = 'batalha'
    global vida
    print(f'Vez de {pPokemon["Nome"]}')
    print('Ataques disponiveis: ')
    print(f'1 - {pPokemon["Nome do ataque 1"]:<25} 2 - {pPokemon["Nome do ataque 2"]}')

    opcao = int(input('Digite aqui: '))
    
    if opcao == 1:
        print(f'{sPokemon["Nome"]} sofreu {pPokemon["Valor do ataque 1"]} de dano')
        sPokemon['HP atual'] = int(sPokemon['HP atual']) - int(pPokemon['Valor do ataque 1'])
        atualizarHP(sPokemon, vindo)
        sleep(1)

        if int(sPokemon['HP atual']) <= 0:
            sPokemon['HP atual'] = 0
            print(f'{sPokemon["Nome"]} está com {sPokemon["HP atual"]} de vida')
            sleep(1)
            atualizarHP(sPokemon, vindo)
            print(f'{sPokemon["Nome"]} foi derrotado')
            print(f'{pPokemon["Nome"]} venceu!')
            vida = False

        elif int(sPokemon['HP atual']) > 0:
            print(f'{sPokemon["Nome"]} está com {sPokemon["HP atual"]} de vida')
            vida = True

    elif opcao == 2:
        print(f'{sPokemon["Nome"]} sofreu {pPokemon["Valor do ataque 2"]} de dano')
        sPokemon['HP atual'] = int(sPokemon['HP atual']) - int(pPokemon['Valor do ataque 2'])
        atualizarHP(sPokemon, vindo)
        sleep(1)

        if int(sPokemon['HP atual']) <= 0:
            sPokemon['HP atual'] = 0
            print(f'{sPokemon["Nome"]} está com {sPokemon["HP atual"]} de vida')
            sleep(1)
            atualizarHP(sPokemon, vindo)
            print(f'{sPokemon["Nome"]} foi derrotado')
            print(f'{pPokemon["Nome"]} venceu!')
            vida = False
                
        elif int(sPokemon['HP atual']) > 0:
            print(f'{sPokemon["Nome"]} está com {sPokemon["HP atual"]} de vida')
            vida = True
    
    return vida

def asPokemon(sPokemon, pPokemon):
    vindo = 'batalha'
    global vida
    print(f'Vez de {sPokemon["Nome"]}')
    print('Ataques disponiveis: ')
    print(f'1 - {sPokemon["Nome do ataque 1"]:<25} 2 - {sPokemon["Nome do ataque 2"]}')

    opcao = int(input('Digite o nome do ataque: '))
    
    if opcao == 1:
        print(f'{pPokemon["Nome"]} sofreu {sPokemon["Valor do ataque 1"]} de dano')
        pPokemon['HP atual'] = int(pPokemon['HP atual']) - int(sPokemon['Valor do ataque 1'])
        atualizarHP(pPokemon, vindo)
        sleep(1)

        if int(pPokemon['HP atual']) <= 0:
            pPokemon['HP atual'] = 0
            print(f'{pPokemon["Nome"]} está com {pPokemon["HP atual"]} de vida')
            sleep(1)
            atualizarHP(pPokemon, vindo)
            print(f'{pPokemon["Nome"]} foi derrotado')
            print(f'{sPokemon["Nome"]} venceu!')
            vida = False
                
        elif int(pPokemon['HP atual']) > 0:
            print(f'{pPokemon["Nome"]} está com {pPokemon["HP atual"]} de vida')
            vida = True

    elif opcao == 2:
        print(f'{pPokemon["Nome"]} sofreu {sPokemon["Valor do ataque 2"]} de dano')
        pPokemon['HP atual'] = int(pPokemon['HP atual']) - int(sPokemon['Valor do ataque 2'])
        atualizarHP(pPokemon, vindo)
        sleep(1)
        
        if int(pPokemon['HP atual']) <= 0:
            pPokemon['HP atual'] = 0
            print(f'{pPokemon["Nome"]} está com {pPokemon["HP atual"]} de vida')
            sleep(1)
            atualizarHP(pPokemon, vindo)
            print(f'{pPokemon["Nome"]} foi derrotado')
            print(f'{sPokemon["Nome"]} venceu!')
            vida = False

        elif int(pPokemon['HP atual']) > 0:
            print(f'{pPokemon["Nome"]} está com {pPokemon["HP atual"]} vida')
            vida = True
    
    return vida

def selecionar(dadosPokemons):
    pCodigo = int(input('Digite o código do primeiro pokemon desejado: '))
    sCodigo = int(input('Digite o código do segundo pokemon desejado: '))

    for pokemon in dadosPokemons:
        if int(pokemon['Número Pokedex']) == pCodigo:
            pPokemon = pokemon

        elif int(pokemon['Número Pokedex']) == sCodigo:
            sPokemon = pokemon
    
    return pPokemon, sPokemon