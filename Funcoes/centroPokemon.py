from .Arquivos.adicionar import atualizarHP, lerPokedex
from time import sleep

def recuperar():
    vindo = 'curar'
    pokedex = lerPokedex()

    print('Deseja curar UM ou TODOS os pokemons?')
    print('1 - Curar um pokemon')
    print('2 - Curar todos os pokemons')
    
    opcao = int(input('Digite aqui: '))

    match opcao:
        case 1:
            print('Qual pokemon você deseja curar?')
            for pokemon in pokedex:
                print(f'{pokemon["Número Pokedex"]} - {pokemon["Nome"]} tem {pokemon["HP atual"]} de vida')
            
            print('Digite o ID do Pokemon')
            opcao = int(input('Digite aqui: '))

            print('Aguarde enquanto curamos seu pokemon!')
            sleep(5)
            print('Saúde restaurada!')
            
            for pokemon in pokedex:
                if pokemon['Número Pokedex'] == opcao:
                    atualizarHP(pokemon, vindo)

        case 2:
            for pokemons in pokedex:
                atualizarHP(pokemons, vindo)

            print('Aguarde enquanto curamos seus pokemon!')
            sleep(5)
            print('Saúde restaurada!')
        
        case _:
            print('Opção inválida!')
