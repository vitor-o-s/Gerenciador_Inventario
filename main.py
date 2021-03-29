import setor
import tkinter as tk
from tkinter import Label, Menu

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
    itemCadastro.add_command(label='Pessoa')#, command=CadastroPessoa)
    itemCadastro.add_separator()
    itemCadastro.add_command(label='Setor', command=setor.CadastroSetor())
    itemCadastro.add_separator()
    itemCadastro.add_command(label='Sair', command=quit)
    menu.add_cascade(label='Cadastro', menu=itemCadastro)
    main.config(menu=menu)
    main.mainloop()
