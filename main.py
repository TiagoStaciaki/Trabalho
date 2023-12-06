from Funcoes.menu import menu
from Classes.treinador import Treinador

Tiago = Treinador("Tiago Elyan Staciaki", 16, "M", "Novato", "Amarela")
Julia = Treinador("Julia Eduarda da Rosa", 16, "F", "Novato", "Vermelha")
Eduardo = Treinador("Eduardo Matheus Venancio", 17, "M", "Novato", "Azul")

print(f'Qual criador você deseja jogar?')
print('-'*23 + 'X' + '-'*23)
print(f'\n1 - {Tiago}\n')
print('-'*23 + 'X' + '-'*23)
print(f'\n2 - {Julia}\n')
print('-'*23 + 'X' + '-'*23)
print(f'\n3 - {Eduardo}\n')
print('-'*23 + 'X' + '-'*23)

opcao = int(input('\nDigite a sua escolha: '))

menu(opcao, Tiago, Julia, Eduardo)