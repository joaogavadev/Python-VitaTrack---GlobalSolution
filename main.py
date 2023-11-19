import getpass
import csv

#inicio do programa


def cadastro():
    print("==============================================================")
    print("Cadastro")
    email_user = input("\n\nEmail: ")

    username = input("nome de usuario: ")

    password = getpass.getpass()

    print("Confirme sua senha novamente:")
    password2 = getpass.getpass()
    cadastro_registro = [email_user, username, password]

    while password != password2:

        print("As senhas não coincidem, Digite sua senha:")
        password = getpass.getpass()

        print("Confirme sua senha novamente:")
        password2 = getpass.getpass()
    else:
        print("Cadastro finalizado.")
        with open(r'C:\Users\gava\Documents\PROGRAMAÇÃO\ARQUIVOS PYTHON\GS\logins.csv', 'a', newline="") as f:
            validador_csv = csv.writer(f)
            validador_csv.writerow(cadastro_registro)

        print("\nCadastro finalizado. Agora você pode fazer login.")
        login()
def login():
    print("==============================================================")
    print("Login\n\n")
    email_user = input("Email: ")
    username = input("Usuário: ")
    password_login = getpass.getpass()

    while not validar_login(username, password_login, email_user):
        login_incorreto = input("Usuario, email ou senha incorretos. Digite 1 para tentar novamente ou Digite 2 para retornar: ")
        if login_incorreto == '2':
            introdução()
            return
        elif login_incorreto == '1':
            email_user = input("\nEmail: ")
            username = input("Usuário: ")
            password_login = getpass.getpass()
        else:
            print("Opção inválida. Digite 1 para tentar novamente ou Digite 2 para retornar.")

    print("\nLogin bem-sucedido!")
    input("Pressione Enter para acessar nosso menu...")
    menu()

def validar_login(username, password, email_user):
    with open(r'C:\Users\gava\Documents\PROGRAMAÇÃO\ARQUIVOS PYTHON\GS\logins.csv', 'r', newline="") as f:
        leitor_csv = csv.reader(f)

        for linha in leitor_csv:
            if len(linha) >= 3 and linha[1] == username and linha[2] == password and linha[0] == email_user:
                return True

        return False
        
def introdução():
    print("==============================================================")
    print("                   Bem-vindo à VitaTrack!")
    print("==============================================================")


    print("Escolha uma opção: \n1. Fazer Login.\n2. Cadastrar\n3. Sair")
    user_choise = input()
    match user_choise:
        case '1':
            login()
        case '2':
            cadastro()
        case '3':
            print("Obrigado por usar a VitaTrack. Até logo!")
        case _:
            print("Opção Invalida, Escolha uma opção válida.")
            introdução()


def menu():
    print("==============================================================")
    print("                           MENU")
    print("==============================================================")

introdução()









