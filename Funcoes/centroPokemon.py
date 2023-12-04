from .Arquivos.adicionar import atualizarHP, lerPokedex

def recuperar():
    vindo = 'curar'
    pokedex = lerPokedex()

    print('Qual pokemon você deseja curar?')
    for pokemon in pokedex:
        print(f'{pokemon["Nome"]} tem {pokemon["HP atual"]} de vida')
    
    print('Digite o nome do Pokemon')
    opcao = input('Digite aqui: ')

    for pokemon in pokedex:
        if pokemon['Nome'] == opcao:
            atualizarHP(pokemon, vindo)
