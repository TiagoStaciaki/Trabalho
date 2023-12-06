from Classes.pokemon import Pokemon
from .Arquivos.adicionar import adicionarPokemon, lerPokedex

def newPokemon(pokedex):

    while True:
        N_HPAtual = 0
        N_nome = input('Digite o nome do novo pokémon: ')
        N_HPTotal = int(input('Digite a VIDA total do pokémon: '))
        N_HPAtual = N_HPTotal
        N_Iniciativa = int(input('Digite iniciativa do pokémon: '))
        N_Tipo1 = input('Digite o tipo 1 do pokémon: ')

        print('O pokémon tem um outro tipo?')
        print('1 - Sim')
        print('2 - Não')
        opcao = int(input('Digite aqui: '))

        match opcao:
            case 1:
                N_Tipo2 = input('Digte o tipo 2 do pokémon: ')
                N_nomeAtaque1 = input('Digite o nome do ataque: ')
                N_valorAtaque1 = int(input('Digite o valor do dano: '))

                print('O pokémon tem um outro ataque?')
                print('1 - Sim')
                print('2 - Não')
                opcao = int(input('Digite aqui: '))

                match opcao:
                    case 1:
                        N_nomeAtaque2 = input('Digite o nome do ataque: ')
                        N_valorAtaque2 = int(input('Digite o valor do dano: '))
                    
                    case 2:
                        N_nomeAtaque2 = 'Nenhum'
                        N_valorAtaque2 = '0'

            case 2:
                N_Tipo2 = 'Nenhum'
                N_nomeAtaque1 = input('Digite o nome do ataque: ')
                N_valorAtaque1 = int(input('Digite o valor do dano: '))

                print('O pokémon tem um outro ataque?')
                print('1 - Sim')
                print('2 - Não')
                opcao = int(input('Digite aqui: '))

                match opcao:
                    case 1:
                        N_nomeAtaque2 = input('Digite o nome do ataque: ')
                        N_valorAtaque2 = int(input('Digite o valor do dano: '))
                    
                    case 2:
                        N_nomeAtaque2 = 'Nenhum'
                        N_valorAtaque2 = '0'

        pokedex.append(Pokemon(N_nome, Npokedex(), N_HPTotal, N_HPAtual, N_Iniciativa, N_Tipo1, N_Tipo2, N_nomeAtaque1, N_valorAtaque1, N_nomeAtaque2, N_valorAtaque2))
        adicionarPokemon(pokedex[-1])

        print('Deseja adicionar outro pokémon?')
        print('1 - Sim')
        print('2 - Não')
        opcao = int(input('Digite aqui: '))
        match opcao:
            case 1:
                continue

            case 2:
                break

def Npokedex():
    pokedex = lerPokedex()
    for pokemon in pokedex:
        UltimoP = pokemon['Número Pokedex']
    UltimoP = int(UltimoP) + 1

    return UltimoP
