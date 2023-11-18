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
        with open(r'C:\Users\gava\Documents\PROGRAMAÇÃO\ARQUIVOS PYTHON\GS\logins.csv', 'w', newline="") as f:
            validador_csv = csv.writer(f)
            validador_csv.writerow(cadastro_registro)

def login():
    print("==============================================================")
    print("Login\n\n")
    email_user = input("Email: ")
    username = input("Usuário: ")
    password_login = getpass.getpass()

    if validar_login(username, password_login, email_user):
        print("Login bem-sucedido!")
    else:
        print("Usuário ou senha incorretos.")

def validar_login(username, password, email_user):
    with open(r'C:\Users\gava\Documents\PROGRAMAÇÃO\ARQUIVOS PYTHON\GS\logins.csv', 'r', newline="") as f:
        leitor_csv = csv.reader(f)

        for linha in leitor_csv:
            if len(linha) >= 3 and linha[1] == username and linha[2] == password and linha[0] == email_user:
                return True

        return False
        
def introdução():
    print("==============================================================")
    print("Seja bem vindo a nossa plataforma VitaTrack!")


    print("\nVocê já é um usuario ou gostaria de se cadastrar? \n-Digite '1' se já for cadastrado. \n-Digite '2' se gostaria de realizar o cadastro)")
    user_choise = input("")
    match user_choise:
        case '1':
            login()
        case '2':
            cadastro()


introdução()








