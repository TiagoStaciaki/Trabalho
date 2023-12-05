from .Arquivos.adicionar import atualizarHP, lerPokedex
from time import sleep

def recuperar():
    vindo = 'curar'
    pokedex = lerPokedex()

    print('Qual pokemon você deseja curar?')
    for pokemon in pokedex:
        print(f'{pokemon["Nome"]} tem {pokemon["HP atual"]} de vida')
    
    print('Digite o nome do Pokemon')
    opcao = input('Digite aqui: ')

    print('Aguarde em quanto curamos seu pokemon!')
    sleep(5)
    print('Saúde restaurada!')
    print()
    for pokemon in pokedex:
        if pokemon['Nome'] == opcao:
            atualizarHP(pokemon, vindo)
