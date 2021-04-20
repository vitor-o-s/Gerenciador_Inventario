import banco
import tkinter as tk
from tkinter import Label, Entry, Button
from functools import partial


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


    labelResult = tk.Label(Setor)  
    labelResult.grid(row=4, column=1) 

    btnIncluir = Button(Setor, text='Incluir', command = partial(FuncaoButton, txtCodigo, txtNomeSetor,txtCodigoCoordenador, labelResult))
    btnIncluir.grid(column=1, row=3)

def FuncaoButton(codigo, setor, nomecoord, labelResult):

    if checkfill(codigo, setor, nomecoord):
        labelResult.config(text="Nome ou Cargo ou Email não foi preenchido. Favor verificar")

    else:
        pass

def checkfill(codigo, setor, nomecoord):

    return codigo.get()=='' or nomecoord.get()=='' or setor.get==''