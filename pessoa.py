import tkinter as tk
from tkinter import Label, Entry, Button
from functools import partial
import banco

def CadastroPessoa():
    Pessoa = tk.Tk()
    
    Pessoa.geometry('400x300') #tamanho tela
    Pessoa.title("Cadastro de Pessoas") # titulo
    # lblCodigo = Label(Pessoa, text='Código:') 
    # lblCodigo.grid(column=0, row=0)
    # txtCodigo = Entry(Pessoa, width=10)
    # txtCodigo.grid(column=1, row=0)
    lblNomePessoa = Label(Pessoa, text='Nome:')
    lblNomePessoa.grid(column=0, row=1)
    txtNomePessoa = Entry(Pessoa, width=50)
    txtNomePessoa.grid(column=1, row=1)
    lblCargo = Label(Pessoa, text='Cargo:')
    lblCargo.grid(column=0, row=2)
    txtCargo = Entry(Pessoa, width=50)
    txtCargo.grid(column=1, row=2)
    lblEmail = Label(Pessoa, text='E-mail:')
    lblEmail.grid(column=0, row=3)
    txtEmail = Entry(Pessoa, width=50)
    txtEmail.grid(column=1, row=3)
    
    labelResult = tk.Label(Pessoa)  
    labelResult.grid(row=7, column=1) 

    btnIncluir = Button(Pessoa, text='Incluir', command = partial(FuncaoButton, txtNomePessoa, txtCargo, txtEmail,labelResult))
    btnIncluir.grid(column=1, row=6)




def FuncaoButton(nome, cargo, email,labelResult):

    if ((nome.get() == '') or (cargo.get() == '' ) or (email.get() == ''))  :
        print(" Nome ou Cargo ou Email não foi preenchido. Favor verificar")
        labelResult.config(text="Nome ou Cargo ou Email não foi preenchido. Favor verificar") 
    else:
        print("Inserir")
        
        banco.salvarpessoa(nome.get(), cargo.get(), email.get())
        labelResult.config(text="Inserido")


    
    