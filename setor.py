import tkinter as tk
from tkinter import Label, Entry

def CadastroSetor():

    Setor = tk.Tk()
    Setor.geometry('400x300')
    Setor.title('Cadastro de Setores')
    lblCodigo = Label(Setor, text='Codigo:')
    lblCodigo.grid(column=0, row=0)
    txtCodigo = Entry(Setor, width=10)
    txtCodigo.grid(column=1, row=0)
    lblNomeSetor = Label(Setor, text='Setor:')
    lblNomeSetor.grid(column=0, row=1)
    txtNomeSetor = Entry(Setor, width=30)
    txtNomeSetor.grid(column=1, row=1)
    lblCodigoCoordenador = Label(Setor, text='Nome Coordenador:')
    lblCodigoCoordenador.grid(column=0, row=2)
    txtCodigoCoordenador = Entry(Setor, width=10)
    txtCodigoCoordenador.grid(column=1, row=2)