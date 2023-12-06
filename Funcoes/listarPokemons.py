from .Arquivos.adicionar import lerPokedex
from time import sleep

def listarPokemons():

    pokedex = lerPokedex()

    for pokemonData in pokedex:

        print(f'Nome: {pokemonData["Nome"]:<10} Número na pokedex: {pokemonData["Número Pokedex"]:<5} Inicicativa: {pokemonData["Iniciativa"]}')
        print(f'Vida total: {pokemonData["HP total"]:<5} Vida atual: {pokemonData["HP atual"]}')
        print(f'Tipo 1: {pokemonData["Tipo 1"]:<10} Tipo 2: {pokemonData["Tipo 2"]}')
        print(f'Nome do primeiro ataque: {pokemonData["Nome do ataque 1"]:<10} Dano: {pokemonData["Valor do ataque 1"]}')
        print(f'Nome do segundo ataque: {pokemonData["Nome do ataque 2"]:<10} Dano: {pokemonData["Valor do ataque 2"]}')
        print('-'*23 + 'x' + '-'*23)
        print()
        sleep(0.01)