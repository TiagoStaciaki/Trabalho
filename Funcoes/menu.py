from .cadastrarPokemons import newPokemon
from .listarPokemons import listarPokemons
from .batalha import batalha
from .centroPokemon import recuperar

treinador = None
pokedex = []

def menu(opcao, Tiago, Julia, Eduardo):
    match opcao:
        case 1:
            print(f'Seja bem vindo: {Tiago.nome}')
            treinador = Tiago
        
        case 2:
            print(f'Seja bem vindo: {Julia.nome}')
            treinador = Julia

        case 3:
            print(f'Seja bem vindo: {Eduardo.nome}')
            treinador = Eduardo

        case _:
            print('Opção inválida!')

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
