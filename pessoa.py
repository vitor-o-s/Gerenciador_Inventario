from tkinter.constants import BOTH, END, LEFT, RIGHT, Y
# from Testes.teste import popup_showinfo
import tkinter as tk
from tkinter import ttk, Label, Button, Entry, Menu, Toplevel, Scrollbar,Listbox,Frame
from functools import partial
import banco
import time
from tkinter.messagebox import showinfo
import pandas as pd
from pandastable import Table

"""     
LISTA DE CORREÇÃO
    
FUNCAO BOTAO CONSULTA: CRIAR UMA NOVA COLUNA "CARGO" PARA OS USUÁRIOS (Pode ser integer ou sting) 
"""

def CadastroPessoa():
    Pessoa = tk.Tk()
    style = ttk.Style(Pessoa)
    style.theme_use('clam')
    Pessoa.geometry('800x600')
    Pessoa.title("Cadastro de Pessoas")
    lblNomePessoa = ttk.Label(Pessoa, text='Nome:')
    lblNomePessoa.grid(column=0, row=1)
    txtNomePessoa = ttk.Entry(Pessoa, width=50)
    txtNomePessoa.grid(column=1, row=1)
    lblEmail = ttk.Label(Pessoa, text='E-mail:')
    lblEmail.grid(column=0, row=3)
    txtEmail = ttk.Entry(Pessoa, width=50)
    txtEmail.grid(column=1, row=3)
    lbldatanascimento = ttk.Label(Pessoa, text='Data de Nascimento:')
    lbldatanascimento.grid(column=0, row=5)
    txtdatanascimento = ttk.Entry(Pessoa, width=50)
    txtdatanascimento.grid(column=1, row=5)
    lblSetor = ttk.Label(Pessoa, text='Setor:')
    lblSetor.grid(column=0, row=7)
    txtSetor = ttk.Entry(Pessoa, width=50)
    txtSetor.grid(column=1, row=7)
    
    labelResult = ttk.Label(Pessoa)  
    labelResult.grid(row=7, column=1) 

    btnIncluir = ttk.Button(Pessoa, text='Incluir', command = partial(FuncaoButtonCadastro, txtNomePessoa, txtEmail,labelResult))
    btnIncluir.grid(column=1, row=6)

def ConsultaPessoa():

    '''
    A função deve conseguir consultar pessoas pelo nome, pelo email ou pelos 2.
    * Caso não seja inserido nenhum informação e clicado no botão "Consultar" deve retornar a lista de todos.
    ** A consulta sem preenchumento dos parâmetros só deve ser permitido enquanto não haver muitos registros de pessoas no sistema
    '''

    Pessoa = tk.Tk()
    
    Pessoa.geometry('800x600')
    Pessoa.title("Consultando Pessoas")
    


    lblNomePessoa = ttk.Label(Pessoa, text='Nome:')
    lblNomePessoa.grid(column=0, row=1)
    txtNomePessoa = ttk.Entry(Pessoa, width=50)
    txtNomePessoa.grid(column=1, row=1)
    
    lblEmail = ttk.Label(Pessoa, text='E-mail:')
    lblEmail.grid(column=0, row=3)
    txtEmail = ttk.Entry(Pessoa, width=50)
    txtEmail.grid(column=1, row=3)
    
    labelResult = ttk.Label(Pessoa)  
    labelResult.grid(row=7, column=1) 

    btnIncluir = ttk.Button(Pessoa, text='Consultar', command = partial(FuncaoButtonConsulta, 
                                                                  txtNomePessoa, 
                                                                  txtEmail, labelResult))
    btnIncluir.grid(column=1, row=6)

def FuncaoButtonCadastro(nome, email,labelResult):

    if checkfill(nome,email):
        showinfo("Campo Vazio", "Os campos não foram preenchidos corretamente")
        # labelResult.config(text="Nome ou Cargo ou Email não foi preenchido. Favor verificar")

    else:
        if mask(email.get())==1:
            resultado = banco.salvarpessoa(nome.get(), email.get(), labelResult)
            if resultado == 1:
                showinfo("Cadastro Sucesso", "Usuario cadastrado com sucesso")
                # labelResult.config(text="Usuario cadastrado com sucesso")
            elif resultado == 0:
                showinfo("Erro 1", "Usuario já existe na tabela")
                # labelResult.config(text="Usuário já existe na tabela")
        else:
            showinfo("Erro 2", "Dominio email inválido")
            # labelResult.config(text="Dominio email invalido")
            return 


def FuncaoButtonConsulta(nome, email, labelResult):
    
    pessoas = banco.ConsultaPessoa(nome.get(), email.get(), labelResult)
    
    colunas = getColumnName()

    # print(colunas)
    # print(list(pessoas[0]))
    listaPessoa = []
    for i in range(0,len(pessoas)):
        listaPessoa.append(list(pessoas[i]))

    df = pd.DataFrame(listaPessoa, columns=colunas)

    if pessoas != None:
        root = tk.Tk()
        style = ttk.Style(root)
        style.theme_use('clam')
        root.geometry('800x600')
        root.title("Lista de Pessoas")
        f = Frame(root)
        f.pack(fill=BOTH,expand=1)
        pt = Table(f, dataframe=df)
        pt.show()

    else:
        showinfo("Window", "resultado não encontrado")
        # labelResult.config(text= "resultado não encontrado")


    ## RETORNA COLUNAS DA TABELA (TODAS)

def getColumnName():
    COLUMN_NAME = banco.QueryColumnPessoa()
    colunas_tabela = []

    if COLUMN_NAME != None: 
        for i in COLUMN_NAME:
            colunas_tabela.append(i[3])
        return colunas_tabela
    else:
        return []

def checkfill(nome, email, data, cod):
    
    return nome.get()=='' or email.get()=='' or data.get()=='' or cod.get()==''

def mask(s):
    lo = s.find('@')
    return checkDomain(s, lo) == 1

def checkDomain(s, lo):
    dominio_email = s[lo:]
    return dominio_email == '@empresa.com.br'