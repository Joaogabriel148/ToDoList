import tkinter as tk
from tkinter import messagebox

def adicionar_tarefa():
    tarefa = entrada_tarefa.get()
    if tarefa:
        lista_tarefas.insert(tk.END, tarefa)
        entrada_tarefa.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Digite uma tarefa válida!")

def remover_tarefa():
    try:
        selecionado = lista_tarefas.curselection()[0]
        lista_tarefas.delete(selecionado)
    except IndexError:
        messagebox.showwarning("Aviso", "Selecione uma tarefa para remover!")

def limpar_tarefas():
    lista_tarefas.delete(0, tk.END)

# Criando a janela principal
root = tk.Tk()
root.title("To-Do List")
root.geometry("300x400")

# Entrada de tarefa
entrada_tarefa = tk.Entry(root, width=40)
entrada_tarefa.pack(pady=10)

# Botões
btn_adicionar = tk.Button(root, text="Adicionar Tarefa", command=adicionar_tarefa)
btn_adicionar.pack()

btn_remover = tk.Button(root, text="Remover Tarefa", command=remover_tarefa)
btn_remover.pack()

btn_limpar = tk.Button(root, text="Limpar Lista", command=limpar_tarefas)
btn_limpar.pack()

# Lista de tarefas
lista_tarefas = tk.Listbox(root, width=40, height=15)
lista_tarefas.pack(pady=10)

# Executando a aplicação
root.mainloop()
