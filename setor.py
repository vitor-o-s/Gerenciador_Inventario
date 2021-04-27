import banco
import tkinter as tk
from tkinter import Label, Entry, Button
from functools import partial


def CadastroSetor():

    Setor = tk.Tk()
    Setor.geometry('400x300')
    Setor.title('Cadastro de Setores')
    lblCodigo = Label(Setor, text='Codigo do setor:')
    lblCodigo.grid(column=0, row=0)
    txtCodigo = Entry(Setor, width=10)
    txtCodigo.grid(column=1, row=0)
    lblNomeSetor = Label(Setor, text='Setor:')
    lblNomeSetor.grid(column=0, row=1)
    txtNomeSetor = Entry(Setor, width=30)
    txtNomeSetor.grid(column=1, row=1)
    lblCodigoCoordenador = Label(Setor, text='Código Coordenador:')
    lblCodigoCoordenador.grid(column=0, row=2)
    txtCodigoCoordenador = Entry(Setor, width=10)
    txtCodigoCoordenador.grid(column=1, row=2)


    labelResult = tk.Label(Setor)  
    labelResult.grid(row=4, column=1) 

    btnIncluir = Button(Setor, text='Incluir', command = partial(FuncaoButton, txtCodigo, txtNomeSetor,txtCodigoCoordenador, labelResult))
    btnIncluir.grid(column=1, row=3)

def FuncaoButton(codigo, setor, codcoord, labelResult):

    if checkfill(codigo, setor, codcoord):
        labelResult.config(text="Nome ou Cargo ou Email não foi preenchido. Favor verificar")

    else:
        resultado = banco.salvarsetor(codigo.get(), setor.get(), codcoord.get(), labelResult)
        if resultado:
            labelResult.config(text = "Setor cadastrado com sucesso!")
        else:
            labelResult.config(text = "O setor ja existe!")

def checkfill(codigo, setor, codcoord):

    return codigo.get()=='' or codcoord.get()=='' or setor.get==''