import banco
import tkinter as tk
from tkinter import Label, Entry, Button
from functools import partial


def CadastroEmpresa():
    Empresa = tk.Tk()
    Empresa.geometry('400x300')
    Empresa.title("Cadastro de Empresa")
    lblCodigo = Label(Empresa, text='Código:')
    lblCodigo.grid(column=0, row=0)
    txtCodigo = Entry(Empresa, width=10)
    txtCodigo.grid(column=1, row=0)
    lblNomeEmpresa = Label(Empresa, text='Nome da Empresa:')
    lblNomeEmpresa.grid(column=0, row=1)
    txtNomeEmpresa = Entry(Empresa, width=50)
    txtNomeEmpresa.grid(column=1, row=1)
    lblTelefone = Label(Empresa, text='Telefone:')
    lblTelefone.grid(column=0, row=2)
    txtTelefone = Entry(Empresa, width=50)
    txtTelefone.grid(column=1, row=2)
    lblCodResponsavel = Label(Empresa, text='codigo do responsavel:')
    lblCodResponsavel.grid(column=0, row=3)
    txtCodResponsavel = Entry(Empresa, width=50)
    txtCodResponsavel.grid(column=1, row=3)


    labelResult = tk.Label(Empresa)  
    labelResult.grid(row=7, column=2) 

    btnIncluir = Button(Empresa, text='Incluir', command=partial(FuncaoButton, txtCodigo, txtNomeEmpresa, txtTelefone, txtCodResponsavel, labelResult))
    btnIncluir.grid(column=2, row=6)

def FuncaoButton(codigo, nomeempresa, tel, codresp, labelResult):

    if checkfill(codigo, nomeempresa, tel, codresp):
        labelResult.config(text="Nome, Cargo ou Email não foi preenchido. Favor verificar")

    else:
        pass

def checkfill(codigo, nomeempresa, tel, codresp):

    return codigo.get()=='' or nomeempresa.get()=='' or tel.get()=='' or codresp.get==''

def masktel(tel):

    return len(tel) >= 8 #versão mascara inicial
