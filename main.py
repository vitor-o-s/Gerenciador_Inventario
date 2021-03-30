import setor, pessoa
import tkinter as tk
from tkinter import Label, Menu

def clickedpessoa():

    return pessoa.CadastroPessoa()

def clickedsetor():

    return setor.CadastroSetor()


if __name__ == "__main__":

    main = tk.Tk()
    main.geometry('800x600')
    main.title("SistemaInventário")
    lbl = Label(main, text="Seja bem vindo")
    lbl.grid(column=0, row=0)
    menu = Menu(main)
    itemCadastro = Menu(menu)
    itemCadastro.add_command(label='Empresa')
    itemCadastro.add_separator()
    itemCadastro.add_command(label='Computador')
    itemCadastro.add_separator()
    itemCadastro.add_command(label='Pessoa', command=clickedpessoa)
    itemCadastro.add_separator()
    itemCadastro.add_command(label='Setor', command=clickedsetor)
    itemCadastro.add_separator()
    itemCadastro.add_command(label='Sair', command=quit)
    menu.add_cascade(label='Cadastro', menu=itemCadastro)
    main.config(menu=menu)
    main.mainloop()
