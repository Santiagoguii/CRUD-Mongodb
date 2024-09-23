import pymongo
from pymongo import MongoClient
from urllib.parse import quote_plus
import os
import tkinter as tk
from tkinter import messagebox

# Conexão com MongoDB
username = "santiagoguii"
password = quote_plus("gp131204")
url = f"mongodb+srv://{username}:{password}@santiagoad.yxldq.mongodb.net/?retryWrites=true&w=majority&appName=SantiagoAD"
client = MongoClient(url)
db = client['agenda']  
collection = db['contatos']

# Credenciais padrão para o login
usuario = "user"
senha = "user123"

# Função de login
def login():
    username_input = username_entry.get()
    password_input = password_entry.get()

    if username_input == usuario and password_input == senha:
        messagebox.showinfo("Login", "Login bem-sucedido!")
        login_frame.pack_forget()
        main_menu()
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos.")

# Função para cadastrar contato
def registrar_contato():
    nome = nome_entry.get()
    telefone = telefone_entry.get()

    if nome and telefone:
        collection.insert_one({"nome": nome, "telefone": telefone})
        messagebox.showinfo("Sucesso", "Contato cadastrado com sucesso!")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos.")

# Função para consultar contato
def consultar_contato():
    nome = nome_entry.get()

    if nome:
        resultado = collection.find_one({"nome": nome})
        if resultado:
            result_label.config(text=f"Nome: {resultado['nome']}\nTelefone: {resultado['telefone']}")
        else:
            messagebox.showwarning("Não encontrado", "Contato não localizado.")
    else:
        messagebox.showerror("Erro", "Digite um nome para consultar.")

# Função para atualizar contato
def atualizar_contato():
    nome = nome_entry.get()
    novo_telefone = telefone_entry.get()

    if nome and novo_telefone:
        resultado = collection.find_one({"nome": nome})
        if resultado:
            collection.update_one({"nome": nome}, {"$set": {"telefone": novo_telefone}})
            messagebox.showinfo("Sucesso", "Contato atualizado com sucesso!")
        else:
            messagebox.showwarning("Não encontrado", "Contato não localizado.")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos.")

# Função para deletar contato
def deletar_contato():
    nome = nome_entry.get()

    if nome:
        resultado = collection.find_one({"nome": nome})
        if resultado:
            collection.delete_one({"nome": nome})
            messagebox.showinfo("Sucesso", "Contato deletado com sucesso!")
        else:
            messagebox.showwarning("Não encontrado", "Contato não localizado.")
    else:
        messagebox.showerror("Erro", "Digite um nome para deletar.")

# Função para consultar todos os contatos
def consultar_todos_contatos():
    clear_window()
    tk.Label(window, text="Todos os Contatos", bg=bg_color, font=("Helvetica", 14)).pack()

    contatos = list(collection.find())
    if contatos:
        for contato in contatos:
            tk.Label(window, text=f"Nome: {contato['nome']} - Telefone: {contato['telefone']}", bg=bg_color, fg="white").pack()
    else:
        tk.Label(window, text="Nenhum contato cadastrado.", bg=bg_color, fg="white").pack()

    tk.Button(window, text="Voltar", command=main_menu, bg=button_color, fg="white").pack(pady=10)

# Menu principal
def main_menu():
    clear_window()

    tk.Label(window, text="Menu Principal", bg=bg_color, font=("Helvetica", 16), fg="white").pack(pady=10)
    tk.Button(window, text="Cadastrar Contato", command=show_register, bg=button_color, fg="white").pack(pady=5)
    tk.Button(window, text="Consultar Contato", command=show_consult, bg=button_color, fg="white").pack(pady=5)
    tk.Button(window, text="Consultar Todos os Contatos", command=consultar_todos_contatos, bg=button_color, fg="white").pack(pady=5)
    tk.Button(window, text="Atualizar Contato", command=show_update, bg=button_color, fg="white").pack(pady=5)
    tk.Button(window, text="Deletar Contato", command=show_delete, bg=button_color, fg="white").pack(pady=5)
    tk.Button(window, text="Sair", command=window.quit, bg=button_color, fg="white").pack(pady=5)

# Função para limpar a tela
def clear_window():
    for widget in window.winfo_children():
        widget.destroy()

# Telas específicas para ações
def show_register():
    clear_window()
    tk.Label(window, text="Cadastrar Contato", bg=bg_color, font=("Helvetica", 14), fg="white").pack()

    tk.Label(window, text="Nome:", bg=bg_color, fg="white").pack()
    global nome_entry
    nome_entry = tk.Entry(window)
    nome_entry.pack()

    tk.Label(window, text="Telefone:", bg=bg_color, fg="white").pack()
    global telefone_entry
    telefone_entry = tk.Entry(window)
    telefone_entry.pack()

    tk.Button(window, text="Salvar", command=registrar_contato, bg=button_color, fg="white").pack(pady=10)
    tk.Button(window, text="Voltar", command=main_menu, bg=button_color, fg="white").pack(pady=5)

def show_consult():
    clear_window()
    tk.Label(window, text="Consultar Contato", bg=bg_color, font=("Helvetica", 14), fg="white").pack()

    tk.Label(window, text="Nome:", bg=bg_color, fg="white").pack()
    global nome_entry
    nome_entry = tk.Entry(window)
    nome_entry.pack()

    global result_label
    result_label = tk.Label(window, text="", bg=bg_color, fg="white")
    result_label.pack()

    tk.Button(window, text="Consultar", command=consultar_contato, bg=button_color, fg="white").pack(pady=10)
    tk.Button(window, text="Voltar", command=main_menu, bg=button_color, fg="white").pack(pady=5)

def show_update():
    clear_window()
    tk.Label(window, text="Atualizar Contato", bg=bg_color, font=("Helvetica", 14), fg="white").pack()

    tk.Label(window, text="Nome:", bg=bg_color, fg="white").pack()
    global nome_entry
    nome_entry = tk.Entry(window)
    nome_entry.pack()

    tk.Label(window, text="Novo Telefone:", bg=bg_color, fg="white").pack()
    global telefone_entry
    telefone_entry = tk.Entry(window)
    telefone_entry.pack()

    tk.Button(window, text="Atualizar", command=atualizar_contato, bg=button_color, fg="white").pack(pady=10)
    tk.Button(window, text="Voltar", command=main_menu, bg=button_color, fg="white").pack(pady=5)

def show_delete():
    clear_window()
    tk.Label(window, text="Deletar Contato", bg=bg_color, font=("Helvetica", 14), fg="white").pack()

    tk.Label(window, text="Nome:", bg=bg_color, fg="white").pack()
    global nome_entry
    nome_entry = tk.Entry(window)
    nome_entry.pack()

    tk.Button(window, text="Deletar", command=deletar_contato, bg=button_color, fg="white").pack(pady=10)
    tk.Button(window, text="Voltar", command=main_menu, bg=button_color, fg="white").pack(pady=5)

#Ajustes de interface
# Configuração da interface de login
window = tk.Tk()
window.title("Sistema de Contatos")

# Tamanho da janela
window.geometry("500x500")

# Cores e fonte padrão
bg_color = "#4B0082"  
button_color = "#8A2BE2"  
window.config(bg=bg_color)

login_frame = tk.Frame(window, bg=bg_color)
login_frame.pack(pady=20)

tk.Label(login_frame, text="Usuário:", bg=bg_color, fg="white").pack()
username_entry = tk.Entry(login_frame)
username_entry.pack()

tk.Label(login_frame, text="Senha:", bg=bg_color, fg="white").pack()
password_entry = tk.Entry(login_frame, show="*")
password_entry.pack()

tk.Button(login_frame, text="Login", command=login, bg=button_color, fg="white").pack(pady=10)

window.mainloop()
