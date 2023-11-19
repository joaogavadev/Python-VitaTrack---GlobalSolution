import getpass
import csv
import time
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

#inicio do programa


def registro_info():
    #adicionar texto
    print("==============================================================")
    print("Registro")

    nome = input("\nDigite seu primeiro nome: ")
    peso = input("Digite seu peso (Em kg): ")
    idade = input("Digite sua idade: ")
    altura = input("Digite sua altura: ")
    container_userinfo = [nome,idade,peso,altura]
    criar_csv_usuario(nome, container_userinfo)

#colunas criadas respectivamente: |NOME - PESO - IDADE - ALTURA|
def criar_csv_usuario(nome, container_userinfo):
    path = f'C:/Users/gava/Documents/PROGRAMAÇÃO/ARQUIVOS PYTHON/GS/csv/user_dados/{nome}_dados.csv'
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        #infos puxadas + convertendo
        container_userinfo = [str(nome), int(container_userinfo[1]), int(container_userinfo[2]), float(container_userinfo[3])]
        writer.writerow(container_userinfo)
    leitor_userinfo(nome)

def leitor_userinfo(nome):
    path = f'C:/Users/gava/Documents/PROGRAMAÇÃO/ARQUIVOS PYTHON/GS/csv/user_dados/{nome}_dados.csv'
    with open(path, 'r', newline='') as f:
        leitor = csv.reader(f)
        for linha in leitor:
            nome, idade, peso, altura = linha
            print(type(str(nome)))
            print(type(int(idade)))
            print(type(int(peso)))
            print(type(float(altura)))


    #adicionar texto
    IMC = (int(peso)/float(altura)** 2)
    IMC_arredondado = round(IMC, 2)
    print(f"Seu IMC é {IMC_arredondado}")
    if IMC_arredondado >= 40:
        print("Seu estado é de Obesidade grau III")
        


    elif IMC_arredondado >= 35 and IMC_arredondado <= 39.9:
        print("Seu estado é de Obesidade grau II")

    elif IMC_arredondado >= 35 and IMC_arredondado <= 39.9:
        print("Seu estado é de Obesidade grau II")

    elif IMC_arredondado >= 30 and IMC_arredondado <= 34.9:
        print("Seu estado é de Obesidade grau I")

    elif IMC_arredondado >= 25 and IMC_arredondado <= 29.9:
        print("Seu estado é de Sobrepeso")

    elif IMC_arredondado >= 18.6 and IMC_arredondado <= 24.9:
        print("Seu estado é Normal.")

    elif IMC_arredondado < 18.5:
        print("Seu estado é Abaixo do normal.")



def cadastro():
    limpar_tela()
    print("==============================================================")
    print("Cadastro")
    email_user = input("\n\nEmail: ")
    username = input("Nome de usuário: ")
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
        with open(r'C:\Users\gava\Documents\PROGRAMAÇÃO\ARQUIVOS PYTHON\GS\csv\logins.csv', 'a', newline="") as f:
            validador_csv = csv.writer(f)
            validador_csv.writerow(cadastro_registro)

        registro_info()

        print("\nCadastro finalizado. Você será redirecionado para o nosso menu em breve... ")
        time.sleep(5)
        menu()
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
    with open(r'C:\Users\gava\Documents\PROGRAMAÇÃO\ARQUIVOS PYTHON\GS\csv\logins.csv', 'r', newline="") as f:
        leitor_csv = csv.reader(f)

        for linha in leitor_csv:
            if len(linha) >= 3 and linha[1] == username and linha[2] == password and linha[0] == email_user:
                return True

        return False
        
def introdução():
    limpar_tela()
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

    print()

introdução()









