import tkinter as tk
from tkinter import Label, Entry, Button
from functools import partial
import banco

def CadastroPessoa():
    Pessoa = tk.Tk()
    
    Pessoa.geometry('400x300')
    Pessoa.title("Cadastro de Pessoas")
    lblNomePessoa = Label(Pessoa, text='Nome:')
    lblNomePessoa.grid(column=0, row=1)
    txtNomePessoa = Entry(Pessoa, width=50)
    txtNomePessoa.grid(column=1, row=1)
    lblEmail = Label(Pessoa, text='E-mail:')
    lblEmail.grid(column=0, row=3)
    txtEmail = Entry(Pessoa, width=50)
    txtEmail.grid(column=1, row=3)
    '''
	nomeCompleto VARCHAR(70) - ja tem
	dataNascimento date, - sem por enquanto
	email VARCHAR(50), - ja tem 
	codSetor INTEGER, - lista de setores disponiveis?
	macETH MACADDR, - sem preenchimento aqui?
	macWLAN MACADDR - sem preenchimento aqui?

    '''
    
    labelResult = tk.Label(Pessoa)  
    labelResult.grid(row=7, column=1) 

    btnIncluir = Button(Pessoa, text='Incluir', command = partial(FuncaoButton, txtNomePessoa, txtEmail,labelResult))
    btnIncluir.grid(column=1, row=6)




def FuncaoButton(nome, email,labelResult):

    if checkfill(nome,email):
        labelResult.config(text="Nome ou Cargo ou Email não foi preenchido. Favor verificar")

    else:
        if mask(email.get())==1:
            resultado = banco.salvarpessoa(nome.get(), email.get(), labelResult)
            if resultado == 1:
                labelResult.config(text="Usuario cadastrado com sucesso")
            elif resultado == 0:
                labelResult.config(text="Usuário já existe na tabela")
        else:
            print("Dominio email invalido")
            return 

def checkfill(nome, email):

    return nome.get()=='' or email.get()=='' 

def mask(s):
    lo = s.find('@')
    return checkDomain(s, lo) == 1

def checkDomain(s, lo):
    dominio_email = s[lo:]
    return dominio_email == '@empresa.com.br'