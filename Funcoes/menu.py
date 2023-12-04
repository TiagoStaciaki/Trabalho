from .cadastrarPokemons import newPokemon
from .listarPokemons import listarPokemons
from .batalha import batalha
from .centroPokemon import recuperar

pokedex = []

def menu():

    while True:
        print('1. Cadastrar Pokemon')
        print('2. Listar Pokemon')
        print('3. Batalha Pokemon')
        print('4. Recuperar Pokemon')
        print('5. Sair')

        opcao = int(input('Digite a opção: '))

        match opcao:
            case 1:
                newPokemon(pokedex)
                
            case 2:
                listarPokemons()

            case 3:
                batalha()

            case 4:
                recuperar()

            case 5:
                break

            case _:
                print('Operação inválida')
