import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_menu():
    limpar_tela()
    print("==============================================================")
    print("                   Bem-vindo à VitaTrack!")
    print("==============================================================")
    print("Escolha uma opção:")
    print("1. Fazer Login")
    print("2. Cadastrar")
    print("3. Sair")

exibir_menu()
