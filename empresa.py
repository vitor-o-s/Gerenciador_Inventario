from tkinter.constants import BOTH, END, LEFT, RIGHT, Y
import banco
import tkinter as tk
from tkinter import ttk, Label, Button, Entry, Menu, Toplevel, Scrollbar,Listbox,Frame
from functools import partial
import pandas as pd
from pandastable import Table

''' MÉTODOS IMPLEMENTADOS:

    - CadastroEmpresa()  #Tela Cadastro
    - ConsultaEmpresa()  #Tela Consulta
    - FuncaoButtonCadastro() #Botao tela Cadastro 
    - FuncaoButtonConsulta() #Botao tela Consulta
    - checkfill() #Verifica se campos vazio
    - masktel()

'''

''' Correções
    -> Na coluna "Código responsável deve verificar na TABELA "PESSOA" se pessoa está cadastrado e atrelar o código

	codEmpresa SERIAL NOT NULL,
	nomeEmpresa VARCHAR(20),
	telefone VARCHAR(13),
	codResponsavel INTEGER	

'''


##############################################################################################################################

########################################## CADASTRO EMPRESA ###################################################################

##############################################################################################################################


def CadastroEmpresa():
    Empresa = tk.Tk()
    style = ttk.Style(Empresa)
    style.theme_use('clam')
    Empresa.geometry('800x600')
    Empresa.title("Cadastro de Empresa")
    
    lblCodigo = ttk.Label(Empresa, text='Código:')
    lblCodigo.grid(column=0, row=0)
    txtCodigo = ttk.Entry(Empresa, width=10)
    txtCodigo.grid(column=1, row=0)
    
    lblNomeEmpresa = ttk.Label(Empresa, text='Nome da Empresa:')
    lblNomeEmpresa.grid(column=0, row=1)
    txtNomeEmpresa = ttk.Entry(Empresa, width=50)
    txtNomeEmpresa.grid(column=1, row=1)
    
    lblTelefone = ttk.Label(Empresa, text='Telefone:')
    lblTelefone.grid(column=0, row=2)
    txtTelefone = ttk.Entry(Empresa, width=50)
    txtTelefone.grid(column=1, row=2)
    
    lblCodResponsavel = ttk.Label(Empresa, text='codigo do responsavel:')
    lblCodResponsavel.grid(column=0, row=3)
    txtCodResponsavel = ttk.Entry(Empresa, width=50)
    txtCodResponsavel.grid(column=1, row=3)


    labelResult = tk.Label(Empresa)  
    labelResult.grid(row=7, column=2) 

    btnIncluir = ttk.Button(Empresa, text='Incluir',
                            command=partial(FuncaoButtonCadastro,
                                         txtCodigo, 
                                         txtNomeEmpresa, 
                                         txtTelefone, 
                                         txtCodResponsavel, labelResult))
    btnIncluir.grid(column=1, row=6)

##############################################################################################################################

########################################## CONSULTA EMPRESA ###################################################################

##############################################################################################################################

def ConsultaEmpresa():
    Empresa = tk.Tk()
    style = ttk.Style(Empresa)
    style.theme_use('clam')
    Empresa.geometry('800x600')
    Empresa.title("Consulta de Empresa")
    
    lblCodigo = ttk.Label(Empresa, text='Código:')
    lblCodigo.grid(column=0, row=0)
    txtCodigo = ttk.Entry(Empresa, width=10)
    txtCodigo.grid(column=1, row=0)
    
    lblNomeEmpresa = ttk.Label(Empresa, text='Nome da Empresa:')
    lblNomeEmpresa.grid(column=0, row=1)
    txtNomeEmpresa = ttk.Entry(Empresa, width=50)
    txtNomeEmpresa.grid(column=1, row=1)
    
    lblTelefone = ttk.Label(Empresa, text='Telefone:')
    lblTelefone.grid(column=0, row=2)
    txtTelefone = ttk.Entry(Empresa, width=50)
    txtTelefone.grid(column=1, row=2)
    
    lblCodResponsavel = ttk.Label(Empresa, text='codigo do responsavel:')
    lblCodResponsavel.grid(column=0, row=3)
    txtCodResponsavel = ttk.Entry(Empresa, width=50)
    txtCodResponsavel.grid(column=1, row=3)


    labelResult = tk.Label(Empresa)  

    btnIncluir = ttk.Button(Empresa, text='Consultar',
                         command=partial(FuncaoButtonConsulta,
                                         txtCodigo, 
                                         txtNomeEmpresa, 
                                         txtTelefone, 
                                         txtCodResponsavel, labelResult))
    btnIncluir.grid(column=1, row=6)
    labelResult.grid(row=7, column=1) 
##############################################################################################################################

########################################## FUNÇÃO BOTÃO CADASTRA EMPRESA ###################################################################

##############################################################################################################################



def FuncaoButtonCadastro(codigo, nomeempresa, tel, codresp, labelResult):
    if checkfill(codigo, nomeempresa, tel, codresp):
        labelResult.config(text="Um dos campos não foi preenchido. Favor verificar")
    else:
        if masktel(tel.get()):
            resultado = banco.salvarempresa(codigo.get(), 
                                            nomeempresa.get(), 
                                            tel.get(), codresp.get(), labelResult)
            if resultado:
                labelResult.config(text="Empresa cadastrada com sucesso!")
            else:
                labelResult.config(text="Empresa ja existente!")
        else:
            labelResult.config(text="Telefone invalido")


##############################################################################################################################

########################################## FUNÇÃO BOTÃO CONSULTA ###################################################################

##############################################################################################################################



def FuncaoButtonConsulta(codigo, nomeempresa, tel, codresp, labelResult):

    empresas = banco.ConsultaEmpresa(codigo.get(), nomeempresa.get(), tel.get(), codresp.get(), labelResult)
    
    colunas = getColumnName()

    listaSetores = []
    print(empresas)
    for i in range(0,len(empresas)):
        listaSetores.append(list(empresas[i]))

    df = pd.DataFrame(listaSetores, columns=colunas)


    if empresas != None:
        root = tk.Tk()
        style = ttk.Style(root)
        style.theme_use('clam')
        root.geometry('800x600')
        root.title("Lista de Empresas")

        f = Frame(root)
        f.pack(fill=BOTH,expand=1)
        pt = Table(f, dataframe=df)
        pt.show()


        # scrollbar = Scrollbar(root)
        # scrollbar.pack(side = RIGHT, fill=Y)
        
        # ListaEmpresa = Listbox(root, yscrollcommand = scrollbar.set, width = 60)
        # for linha in range(0,len(empresas)):
        #     ListaEmpresa.insert(END, empresas[linha])            
        
        # ListaEmpresa.pack(side = LEFT, fill = BOTH)
        # scrollbar.config(command= ListaEmpresa.yview)
        
        # labelResult.config(text = "Retorno Consulta")

    else:
        labelResult.config(text = "Empresa não encontrado")


def checkfill(codigo, nomeempresa, tel, codresp):
    if codigo.get()=='' or nomeempresa.get()=='' or tel.get()=='' or codresp.get()=='':
        return True
    else:
        return False

def masktel(tel):

    return len(tel) >= 8 #versão mascara inicial

def getColumnName():
    COLUMN_NAME = banco.QueryColumnEmpresa()
    colunas_tabela = []

    if COLUMN_NAME != None: 
        for i in COLUMN_NAME:
            colunas_tabela.append(i[3])
        return colunas_tabela
    else:
        return []