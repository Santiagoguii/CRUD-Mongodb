import pymongo
from pymongo import MongoClient
from urllib.parse import quote_plus
import os

username = "santiagoguii"
password = quote_plus("gp131204")

url = f"mongodb+srv://{username}:{password}@santiagoad.yxldq.mongodb.net/?retryWrites=true&w=majority&appName=SantiagoAD"

client = MongoClient(url)
db = client['agenda']  
collection = db['contatos']

# Credenciais padrão para o login
usuario = "user"
senha = "user123"

# Função para efetuar login
def login():
    print("\n----------LOGIN----------")
    username = input("Usuário: ")
    password = input("Senha: ")

    if username == usuario and password == senha:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(">>>>Login bem-sucedido!\n")
        main()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n>>>>Usuário ou senha incorretos.")
        login()

# Função para cadastrar contato
def registrar_contato():
    print("\n----------CADASTRO DE CONTATO----------")
    try:
        nome = input("Nome completo: ")
        telefone = input("Telefone: ")

        collection.insert_one({
            "nome": nome,
            "telefone": telefone,
        })
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Contato cadastrado com sucesso!\n")
    except Exception as e:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Erro ao cadastrar contato:", e)

# Função para consultar contato
def consultar_contato():
    print("\n----------CONSULTAR CONTATO----------")
    nome = input("Digite o nome do contato: ")

    try:
        resultado = collection.find_one({"nome": nome})
        if resultado:
            print("\n>>>>Dados do contato:")
            print(f"Nome: {resultado['nome']}")
            print(f"Telefone: {resultado['telefone']}\n")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Contato não localizado")
    except Exception as e:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Erro ao consultar contato:", e)

# Função para consultar todos os contatos
def consultar_todos_contatos():
    print("\n----------CONSULTAR TODOS OS CONTATOS----------")
    try:
        contatos = list(collection.find())  # Converte o cursor em uma lista
        if contatos:
            for contato in contatos:
                print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}")
            print("\n")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Nenhum contato cadastrado.")
    except Exception as e:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Erro ao consultar contatos:", e)

# Função para atualizar contato
def atualizar_contato():
    print("\n----------ATUALIZAR CONTATO----------")
    nome = input("Digite o nome do contato: ")

    try:
        resultado = collection.find_one({"nome": nome})
        if resultado:
            novo_telefone = input("[Atualizando] Novo telefone: ")

            collection.update_one({"nome": nome}, {
                "$set": {
                    "telefone": novo_telefone,
                }
            })
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Contato atualizado com sucesso!\n")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n>>>>Contato não encontrado.\n")
    except Exception as e:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Erro ao atualizar contato:", e)

# Função para deletar contato
def deletar_contato():
    print("\n----------DELETAR CONTATO----------")
    nome = input("Informe o nome do contato: ")

    try:
        resultado = collection.find_one({"nome": nome})

        if resultado:
            collection.delete_one({"nome": nome})
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Contato deletado com sucesso!\n")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n>>>>Contato não encontrado.\n")
    except Exception as e:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Não foi possível deletar o contato:", e)

# Menu interativo com opções CRUD
def main():
    opcao = 0
    while opcao != 9:
        print("----------CONTATOS----------")
        print("\n[1] Cadastrar Contato\n[2] Consultar Contato\n[3] Consultar Todos os Contatos\n[4] Atualizar Contato\n[5] Deletar Contato\n[9] Sair")
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            registrar_contato()
        elif opcao == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            consultar_contato()
        elif opcao == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            consultar_todos_contatos()
        elif opcao == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            atualizar_contato()
        elif opcao == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            deletar_contato()
        elif opcao == 9:
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Opção inválida. Por favor, escolha uma opção válida.\n")

# Chamada para função de login
login()