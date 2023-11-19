import getpass
import csv
import time
import os

#inicio do programa
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')



def registro_info():
    limpar_tela()
    global nome

    print("==============================================================")
    print("Registro")
    print("Bem-vindo ao VitaTrack! Vamos começar registrando algumas informações.")

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

    print("\nCalculando seu Índice de Massa Corporal (IMC)...")
    time.sleep(5)
    IMC = (int(peso)/float(altura)** 2)
    IMC_arredondado = round(IMC, 2)
    print(f"\nSeu IMC é {IMC_arredondado}")
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

    print("\nVocê tem ja tem o costume de praticar exercicios fisicos?")
    input("1. Sim\n2. Não\n")
    print("Com qual intensidade?")
    input("1. De 1 a 2 vezes na semana.\n2. De 3 a 4 vezes na semana\n3. De 5 a 6 vezes na semana.\n4. Todos os dias da semana.\n5. Não pratico atividade fisica.\n")
    print("Possui algum historico médico importante?")
    hst_medico = input("1. Sim\n2. Não\n")
    match hst_medico:
        case '1':
            print("Alguma doença crônica?")
            doença_crnc = input("1. Sim\n2. Não\n")
            match doença_crnc:
                case '1':
                    print("Qual dessas?")
                    rps = input("1. Diabetes\n2. Hipertensão\n3. Asma\n4. Artrite\n5. Nenhuma das opções\n")
                    if rps == "5":
                        input("Por favor, escreva o nome da doença: ")
                    print("Algum histórico de lesão?")
                    input("1. Sim\n2. Não\n")




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

        print("\nRegistro finalizado. Você será redirecionado para o nosso menu em breve... ")
        time.sleep(5)
        menu(username)
def login():
    global username
    limpar_tela()
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
    menu(username)

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
    print("                  Bem-vindo ao VitaTrack!")
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


def treino_personalizado(username):
    limpar_tela()
    print("==============================================================")
    print("                     SEU TREINO")
    print("\nBem vindo à sua sessão de treino.")
    esc = input("\nQual seu objetivo de treino?\n1. Perder peso\n2. Ganhar massa.\n3. Voltar\n")
    match esc:
        case '1':
            treino_perder_peso()
        case '2':
            treino_ganhar_massa()
        case '3':
            menu(username)

            
    
def imc_abaixo():
    limpar_tela()
    dieta_abaixo =      """
 ============== DIETA 1 - ABAIXO DO NORMAL ==============

Objetivo: Ganho de peso saudável.

Refeições Sugestivas:

Café da Manhã:
- Aveia cozida com leite integral e frutas (banana, morangos).
- Ovos mexidos com abacate.

Lanche da Manhã:
- Iogurte grego natural com granola.

Almoço:
- Frango grelhado ou tofu para opção vegetariana.
- Quinoa ou arroz integral.
- Legumes cozidos no vapor (brócolis, cenoura).

Lanche da Tarde:
- Mix de nozes (amêndoas, castanhas).

Jantar:
- Salmão assado.
- Batata-doce assada.
- Salada verde com azeite de oliva.

Hidratação:
- Beba água regularmente ao longo do dia.

========================================================
"""

    print(dieta_abaixo)
    input("\nPressione Enter para Voltar...")
    dietas_personalizadas()


def imc_Normal():
    limpar_tela()
    dieta_imc_normal = """
============== DIETA 2 - IMC NORMAL ==============

Objetivo: Manutenção do peso saudável.

Refeições Sugestivas:

Café da Manhã:
- Smoothie de frutas com iogurte grego.
- Torrada integral com abacate.

Lanche da Manhã:
- Maçã ou pera.

Almoço:
- Peito de frango grelhado ou filé de peixe.
- Quinoa ou arroz integral.
- Salada mista com vegetais diversos.

Lanche da Tarde:
- Iogurte natural com morangos.

Jantar:
- Omelete com vegetais (espinafre, tomate, cogumelos).
- Batata-doce ou arroz integral.

Hidratação:
- Água, chás de ervas sem açúcar.

==================================================
"""

    print(dieta_imc_normal)

    input("\nPressione Enter para Voltar...")
    dietas_personalizadas()

def imc_sobrepeso():
    limpar_tela()
    dieta_sobrepeso = """
============== DIETA 3 - IMC SOBREPESO ==============

Refeições Sugestivas:

Café da Manhã:
- Aveia cozida com frutas frescas.
- Omelete de claras de ovo com espinafre.

Lanche da Manhã:
- Um punhado de amêndoas.

Almoço:
- Peito de frango grelhado.
- Quinoa ou arroz integral em porções moderadas.
- Legumes cozidos ou salada verde.

Lanche da Tarde:
- Iogurte grego sem açúcar.

Jantar:
- Salmão grelhado.
- Batata-doce assada.
- Legumes no vapor.

Hidratação:
- Água, chás de ervas sem açúcar.
"""

    print(dieta_sobrepeso)
    input("Pressione Enter para retornar...")
    dietas_personalizadas()

def imc_obesidade1():
    limpar_tela()
    dieta_obesidade_grau_1 = """
============== DIETA 4 - IMC OBESIDADE GRAU I ==============

Refeições Sugestivas:

Café da Manhã:
- Smoothie de vegetais com proteína em pó.
- Torrada integral com abacate.

Lanche da Manhã:
- Maçã ou pera.

Almoço:
- Peito de frango grelhado.
- Quinoa ou arroz integral (quantidade controlada).
- Salada verde com azeite de oliva.

Lanche da Tarde:
- Iogurte grego natural com um punhado de frutas vermelhas.

Jantar:
- Filé de peixe assado.
- Legumes no vapor.
- Batata-doce ou quinoa.

Hidratação:
- Água, chás de ervas sem açúcar.
"""
    print("===========================================================")
    print(dieta_obesidade_grau_1)
    print("\nPressione Enter para retornar...")
    dietas_personalizadas()


def imc_obesidade2_3():
    limpar_tela()
    dieta_obesidade_grau2_3 = """
============== DIETA 5, 6 - IMC OBESIDADE GRAU II e III ==============
Objetivo: Perda de peso significativa com orientação médica.

Refeições Sugestivas:

Café da Manhã:
- Omelete de claras de ovo com espinafre.
- Aveia cozida com frutas frescas.

Lanche da Manhã:
- Um punhado de amêndoas ou nozes.

Almoço:
- Peito de frango grelhado.
- Quinoa ou arroz integral em porções controladas.
- Salada verde com vegetais variados.

Lanche da Tarde:
- Iogurte grego natural com um punhado de frutas vermelhas.

Jantar:
- Salmão grelhado.
- Legumes no vapor.
- Batata-doce ou quinoa.

Hidratação:
- Água, chás de ervas sem açúcar.
"""
    print("======================================================================")
    print(dieta_obesidade_grau2_3)
    print("\nPressione Enter para retornar...")
    dietas_personalizadas()


def dietas_personalizadas():
    limpar_tela()
    print("==============================================================")
    print("                DIETAS PERSONALIZADAS")
    print("Para personalizar sua dieta digite qual o nivel do seu IMC: ")
    esc = input("1. Abaixo do normal \n2. Normal \n3. Sobrepeso\n4. Obesidade grau I\n5. Obesidade grau II\n6.Obesidade grau III\n7. Voltar\n")
    match esc:
        case '1':
            imc_abaixo()
            
        case '2':
            imc_Normal()

        case '3':
            imc_sobrepeso()

        case '4':
            imc_obesidade1()

        case '5':
            imc_obesidade2_3()

        case '6':
            imc_obesidade2_3()

        case '7':
            menu(username)


def treino_ganhar_massa():
    limpar_tela()
    print("==============================================================")
    print("            EXERCICIOS PARA GANHAR MASSA")
    print("Para personalizar seu programa de exercicios fisicos digite qual o nivel do seu IMC: ")
    esc = input("1. Abaixo do normal\n2. Normal\n3. Sobrepeso\n4. Obesidade grau I ou superior\n5. Voltar\n")
    match esc:
        case '1':
            treino_massa1()
            
        case '2':
            treino_massa2()

        case '3':
            treino_massa3()

        case '4':
            treino_massa4()

        case '5':
            menu(username)


def treino_massa1():
    limpar_tela()
    treino_abaixo_do_normal = """
Treino para IMC Abaixo do Normal:

Objetivo: Ganho de peso saudável.

1. Treino Cardiovascular (opcional):
   - Caminhada leve: 20 minutos, 2 vezes por semana.

2. Treino de Resistência:
   - Levantamento de peso moderado: 3 vezes por semana.
   - Exercícios: agachamentos, supino, flexões, abdominais.

3. Treino de Hipertrofia:
   - Séries e repetições moderadas: 2 vezes por semana.
   - Exercícios: leg press, rosca direta, tríceps pulley.

4. Descanso Ativo:
   - Dias de descanso incluem atividades leves como caminhada ou ioga.
"""
    print(treino_abaixo_do_normal)
    input("Pressione Enter para voltar...")
    treino_ganhar_massa()


def treino_massa2():
    limpar_tela()
    treino_normal = """
Treino para IMC Normal:

Objetivo: Manutenção do peso saudável.

1. Treino Cardiovascular:
   - Corrida leve: 30 minutos, 3 vezes por semana.

2. Treino de Resistência:
   - Levantamento de peso moderado: 3 vezes por semana.
   - Exercícios: agachamentos, supino, remada, abdominais.

3. Treino de Hipertrofia (opcional):
   - Séries e repetições moderadas: 2 vezes por semana.
   - Exercícios: leg press, rosca direta, tríceps pulley.

4. Descanso Ativo:
   - Dias de descanso incluem atividades leves como caminhada ou ioga.
"""
    print(treino_normal)
    input("Pressione Enter para voltar...")
    treino_ganhar_massa()

def treino_massa3():
    treino_sobrepeso = """
Treino para IMC Sobrepeso:

Objetivo: Ganho de massa muscular com foco na saúde.

1. Treino Cardiovascular:
   - Esteira: 20 minutos, 3 vezes por semana.

2. Treino de Resistência:
   - Levantamento de peso moderado: 4 vezes por semana.
   - Exercícios: agachamentos, supino, levantamento terra, flexões, abdominais.

3. Treino de Hipertrofia:
   - Séries e repetições moderadas: 3 vezes por semana.
   - Exercícios: leg press, rosca direta, tríceps pulley, elevação lateral.

4. Descanso Ativo:
   - Dias de descanso incluem atividades leves como caminhada ou ioga.
"""
    print(treino_sobrepeso)
    input("Pressione Enter para voltar...")
    treino_ganhar_massa()

def treino_massa4():
    treino_obesidade_grau_1_ou_superior = """
Treino para IMC Obesidade Grau I ou superior:

Objetivo: Ganho de massa muscular com orientação médica.

1. Treino Cardiovascular:
   - Bicicleta ergométrica: 20 minutos, 2 vezes por semana.

2. Treino de Resistência:
   - Levantamento de peso moderado: 4 vezes por semana.
   - Exercícios: agachamentos, supino, levantamento terra, flexões, abdominais.

3. Treino de Hipertrofia:
   - Séries e repetições moderadas: 3 vezes por semana.
   - Exercícios: leg press, rosca direta, tríceps pulley, elevação lateral.

4. Descanso Ativo:
   - Dias de descanso incluem atividades leves como caminhada ou ioga.
"""
    print(treino_obesidade_grau_1_ou_superior)
    input("Pressione Enter para voltar...")
    treino_ganhar_massa()


def treino1():
    limpar_tela()
    treino_sobrepeso = """
Treino para IMC Sobrepeso:

Objetivo: Perda de peso gradual e saudável.

1. Treino Cardiovascular:
   - Caminhada rápida: 30 minutos, 3 vezes por semana.
   - Corrida leve: 20 minutos, 2 vezes por semana.

2. Treino de Resistência:
   - Treino de circuito com pesos leves: 3 vezes por semana.
   - Exercícios: agachamentos, lunges, flexões, abdominais.

3. Alongamento:
   - Sessões de alongamento: 10 minutos após cada treino.

Lembre-se de consultar um profissional de saúde antes de iniciar qualquer programa de treino.
"""
    print(treino_sobrepeso)
    input("Pressione Enter para voltar...")
    treino_personalizado(username)

def treino2():
    limpar_tela()
    treino_obesidade_grau_1 = """
Treino para IMC Obesidade Grau I:

Objetivo: Perda de peso gradual e controle de ingestão calórica.

1. Treino Cardiovascular:
   - Esteira ou bicicleta: 30 minutos, 4 vezes por semana.
   - Treino intervalado de alta intensidade (HIIT): 20 minutos, 2 vezes por semana.

2. Treino de Resistência:
   - Treino de pesos moderados: 3 vezes por semana.
   - Exercícios: agachamentos, levantamento terra, supino, abdominais.

3. Alongamento:
   - Sessões de alongamento: 15 minutos após cada treino.

Lembre-se de consultar um profissional de saúde antes de iniciar qualquer programa de treino.
"""
    print(treino_obesidade_grau_1)
    input("Pressione Enter para voltar...")
    treino_personalizado(username)

def treino3_4():
    limpar_tela()
    treino_obesidade_grau_3_ou_4 = """
Treino para IMC Obesidade Grau II ou III:

Objetivo: Perda de peso significativa com orientação médica.

1. Treino Cardiovascular:
   - Bicicleta ergométrica ou elíptico: 40 minutos, 5 vezes por semana.
   - Treino intervalado de alta intensidade (HIIT): 30 minutos, 3 vezes por semana.

2. Treino de Resistência:
   - Treino de pesos pesados: 4 vezes por semana.
   - Exercícios: agachamentos, levantamento terra, supino, remada, abdominais.

3. Alongamento:
   - Sessões de alongamento: 20 minutos após cada treino.

Lembre-se de consultar um profissional de saúde antes de iniciar qualquer programa de treino.
"""
    print(treino_obesidade_grau_3_ou_4)
    input("Pressione Enter para voltar...")
    treino_personalizado(username)
    

def treino_perder_peso():
    limpar_tela()
    print("==============================================================")
    print("            EXERCICIOS PARA PERDA DE PESO")
    print("\nPara personalizar seu programa de exercicios fisicos digite qual o nivel do seu IMC: ")
    esc = input("1. Sobrepeso\n2. Obesidade grau I\n3. Obesidade grau II\n4. Obesidade grau III\n5. Voltar\n")
    match esc:
        case '1':
            treino1()
            
        case '2':
            treino2()

        case '3':
            treino3_4()

        case '4':
            treino3_4()

        case '5':
            treino_personalizado(username)

def perder_peso():
    print("\nSe o seu objetivo é perder peso, temos as seguintes funcionalidades: ")
    print("1. Planos de Dietas Personalizados\n2. Monitoramento de água\n3. Exercicios para perda de peso\n4. Voltar")
    esc = input()
    match esc:
        case '1':
            dietas_personalizadas()
        case '2':
            print("x")
        case '3':
            treino_perder_peso()
        case '4':
            dietas()
        case _:
            print("Opção invalida.")
            perder_peso()

def ganhar_massa():
    print("Se o seu objetivo é ganhar massa, temos as seguintes funcionalidades: ")
    print("1. Planos de Dietas Personalizados\n2. Exercicios para ganho de massa.")
    esc = input()
    match esc:
        case '1':
            dietas_personalizadas()
        case '2':
            treino_ganhar_massa()


def dietas():
    limpar_tela()
    print("==============================================================")
    print("                 DIETAS E REFEIÇÕES")
    print("Bem vindo a sessão de dietas e refeições")
    print("Qual seu objetivo de dieta?")
    esc = input("\n1. Perder peso\n2. Ganhar massa\n")
    match esc:
        case '1':
            perder_peso()
        case '2':
            print("x")






def meds():
    print("==============================================================")
    print("                 SEUS MEDICAMENTOS")


def atendimento_presencial():
    print("==============================================================")
    print("               AGENDA DE ATENDIMENTO")


def atendimento_online():
    print("==============================================================")
    print("            ATENDIMENTO MEDICO ONLINE")


def menu(username):
    limpar_tela()
    print("==============================================================")
    print("                           MENU")
    print("==============================================================")
    print(f"Bem vindo, {username}")
    

    print("1. Treino Personalizado\n2. Dietas e refeições\n3. Medicamentos\n4. Agendar atendimento medico presencial\n5. Atendimento medico Online\n6. LogOut")
    escolha_menu = input()
    match escolha_menu:
        case '1':
            treino_personalizado(username)
        case '2':
            dietas()
        case '3':
            meds()
        case '4':
            atendimento_presencial()
        case '5':
            atendimento_online()
        case '6':
            print("Obrigado por usar a VitaTrack. Até logo!")
        case '5':
            atendimento_online()


introdução()









