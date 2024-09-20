import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

# Estabelecendo conexão com o MongoDB
client = MongoClient('localhost', 27017)
db = client['Locadora']  # Criando ou acessando o banco de dados
collection = db['clientes']  # Criando ou acessando a coleção de clientes

# Menu inicial para escolher entre login, cadastro e alterar senha
def inicial():
    opcao = 0
    while opcao != 9:
        print("\n----------BEM-VINDO----------")
        print("\n[1] Efetuar Login\n[2] Cadastrar Conta\n[3] Alterar Senha\n[9] Encerrar")
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            login()
        elif opcao == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            RegistrarConta()
        elif opcao == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            AlterarSenha()
        elif opcao == 9:
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Opção inválida. Por favor, escolha uma opção válida.\n")

# Função para efetuar login
def login():
    print("\n----------LOGIN----------")
    CPF = input("Informe o CPF: ")
    senha = input("Senha: ")

    # Validando CPF e Senha
    try:
        resultado = collection.find_one({"CPF": CPF, "senha": senha})

        if resultado:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(">>>>Login bem-sucedido!\n")
            main()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n>>>>CPF ou senha incorretos.")
            inicial()
    except Exception as e:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Erro ao efetuar login:", e)

# Função para alterar a senha da conta
def AlterarSenha():
    print("\n----------ALTERAR SENHA----------")
    CPF = input("Informe o CPF: ")
    senha = input("Senha: ")

    # Validando CPF e Senha
    try:
        resultado = collection.find_one({"CPF": CPF, "senha": senha})

        if resultado:
            key = input("Digite a sua nova senha: ")
            collection.update_one({"CPF": CPF}, {"$set": {"senha": key}})
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Senha alterada com sucesso!\n")
            inicial()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n>>>>CPF ou senha incorretos.")
            inicial()
    except Exception as e:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Erro ao alterar a senha:", e)

# Função para cadastrar cliente
def RegistrarConta():
    print("\n----------CADASTRO----------")
    try:
        nome = input("Nome completo: ")
        CPF = input("CPF: ")
        endereco = input("Endereço: ")
        telefone = input("Telefone: ")
        email = input("E-mail: ")
        senha = input("Senha: ")

        collection.insert_one({
            "nome": nome,
            "CPF": CPF,
            "endereco": endereco,
            "telefone": telefone,
            "email": email,
            "senha": senha
        })
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Conta cadastrada com sucesso!\n")
    except Exception as e:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Erro ao cadastrar conta:", e)

# Função para consultar conta do cliente
def ConsultarConta():
    print("\n----------CONSULTAR CONTA----------")
    key = input("Digite seu CPF: ")

    try:
        resultado = collection.find_one({"CPF": key})
        if resultado:
            print("\n>>>>Dados do cliente:")
            print(f"Nome completo: {resultado['nome']}")
            print(f"CPF: {resultado['CPF']}")
            print(f"Endereço: {resultado['endereco']}")
            print(f"Telefone: {resultado['telefone']}")
            print(f"E-mail: {resultado['email']}")
            print(f"Senha: {resultado['senha']}")
            print("\n")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Cliente não localizado")
    except Exception as e:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Erro ao consultar conta:", e)

# Função para atualizar dados do cliente
def AtualizarConta():
    print("\n----------ATUALIZAR DADOS----------")
    key = input("Digite seu CPF: ")

    try:
        resultado = collection.find_one({"CPF": key})
        if resultado:
            nome = input("[Atualizando] Nome completo: ")
            endereco = input("[Atualizando] Endereço: ")
            telefone = input("[Atualizando] Telefone: ")
            email = input("[Atualizando] E-mail: ")
            senha = input("[Atualizando] Senha: ")

            collection.update_one({"CPF": key}, {
                "$set": {
                    "nome": nome,
                    "endereco": endereco,
                    "telefone": telefone,
                    "email": email,
                    "senha": senha
                }
            })
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Dados atualizados com sucesso!\n")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n>>>>CPF incorreto.\n")
    except Exception as e:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Erro ao atualizar dados:", e)

# Função para deletar conta do cliente
def DeletarConta():
    print("\n----------DELETAR CONTA----------")
    CPF = input("Informe o CPF: ")
    senha = input("Senha: ")

    try:
        resultado = collection.find_one({"CPF": CPF, "senha": senha})

        if resultado:
            collection.delete_one({"CPF": CPF})
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Conta deletada com sucesso!\n")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n>>>>CPF ou senha incorretos.\n")
    except Exception as e:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Não foi possível deletar a conta:", e)

# Menu interativo com opções CRUD
def main():
    opcao = 0
    while opcao != 9:
        print("----------LOCADORA----------")
        print("\n[1] Cadastar Conta\n[2] Consultar Conta\n[3] Atualizar Dados\n[4] Deletar Conta\n[9] Sair")
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            RegistrarConta()
        elif opcao == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            ConsultarConta()
        elif opcao == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            AtualizarConta()
        elif opcao == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            DeletarConta()
        elif opcao == 9:
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Opção inválida. Por favor, escolha uma opção válida.\n")

# Chamada para função inicial (login e cadastro)
inicial()
