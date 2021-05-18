from tkinter.constants import BOTH, END, LEFT, RIGHT, Y
import banco
import tkinter as tk
from tkinter import ttk, Label, Button, Entry, Menu, Toplevel, Scrollbar,Listbox,Frame
from functools import partial
import pandas as pd
from pandastable import Table



''' MÉTODOS IMPLEMENTADOS:

    - CadastroSetor() #Tela Cadastro
    - ConsultaSetor() #Tela Consulta
    - FuncaoButtonCadastro() #Botao tela Cadastro
    - FuncaoButtonConsulta() #Botao tela Consulta
    - checkfill() #Verifica se campos vazio


        TABELA 

    codSetor SERIAL NOT NULL,
	codCoordenador INTEGER, 
	nomeSetor VARCHAR(20)

'''

""" LISTA CORREÇÃO:

 -> Precisa ser inserido coluna "CARGO" na TABELA [Pessoa] para cadastrar um novo setor


"""

#####################################################################
############################ CADASTRO SETOR #########################
#####################################################################

def CadastroSetor():

    Setor = tk.Tk()
    style = ttk.Style(Setor)
    style.theme_use('clam')
    Setor.geometry('800x600')
    Setor.title('Cadastro de Setores')
    lblCodigo = ttk.Label(Setor, text='Codigo do setor:')
    lblCodigo.grid(column=0, row=0)
    txtCodigo = ttk.Entry(Setor, width=30)
    txtCodigo.grid(column=1, row=0)
    lblNomeSetor = ttk.Label(Setor, text='Setor:')
    lblNomeSetor.grid(column=0, row=1)
    txtNomeSetor = ttk.Entry(Setor, width=30)
    txtNomeSetor.grid(column=1, row=1)
    lblCodigoCoordenador = ttk.Label(Setor, text='Código Coordenador:')
    lblCodigoCoordenador.grid(column=0, row=2)
    txtCodigoCoordenador = ttk.Entry(Setor, width=30)
    txtCodigoCoordenador.grid(column=1, row=2)


    labelResult = ttk.Label(Setor)  
    labelResult.grid(row=4, column=1) 

    btnIncluir = ttk.Button(Setor, text='Incluir', command = partial(FuncaoButtonCadastro, 
                                                                 txtCodigo, 
                                                                 txtNomeSetor, 
                                                                 txtCodigoCoordenador, labelResult))
    btnIncluir.grid(column=1, row=3)

####################################################################################
############################ CONSULTA SETOR #########################################
####################################################################################
# Ajeitar
def ConsultaSetor():
    Setor = tk.Tk()
    style = ttk.Style(Setor)
    style.theme_use('clam')
    Setor.geometry('800x600')

    Setor.title('Consulte Setores')
    lblCodigo = ttk.Label(Setor, text='Codigo do setor:')
    lblCodigo.grid(column=0, row=0)
    txtCodigo = ttk.Entry(Setor, width=30)
    txtCodigo.grid(column=1, row=0)
    
    lblNomeSetor = ttk.Label(Setor, text='Setor:')
    lblNomeSetor.grid(column=0, row=1)
    txtNomeSetor = ttk.Entry(Setor, width=30)
    txtNomeSetor.grid(column=1, row=1)

    labelResult = ttk.Label(Setor)  
    labelResult.grid(row=4, column=1) 

    btnIncluir = ttk.Button(Setor, text='Consultar', command = partial(FuncaoButtonConsulta, txtCodigo, txtNomeSetor,labelResult))
    btnIncluir.grid(column=1, row=3)



####################################################################################
############################ FUNÇÃO BOTÃO CADASTRO ##################################
####################################################################################
def FuncaoButtonCadastro(codigoSetor, setor, codcoord, labelResult):

    if checkfill(codigoSetor, setor, codcoord):
        labelResult.config(text="Nome ou Cargo ou Email não foi preenchido. Favor verificar")

    else:
        resultado = banco.salvarsetor(codigoSetor.get(), setor.get(), codcoord.get(), labelResult)
        if resultado:
            labelResult.config(text = "Setor cadastrado com sucesso!")
        else:
            labelResult.config(text = "O setor ja existe!")


####################################################################################
############################# FUNÇÃO BOTÃO CONSULTA #################################
####################################################################################
def FuncaoButtonConsulta(codigoSetor, setor, labelResult):

    setores = banco.ConsultaSetor(codigoSetor.get(), setor.get(), labelResult)

    colunas = getColumnName()

    listaSetores = []
    print(setores)
    for i in range(0,len(setores)):
        listaSetores.append(list(setores[i]))

    df = pd.DataFrame(listaSetores, columns=colunas)

    if setores != None:
        root = tk.Tk()
        style = ttk.Style(root)
        style.theme_use('clam')
        root.geometry('800x600')
        root.title("Lista de Setores")
        

        f = Frame(root)
        f.pack(fill=BOTH,expand=1)
        pt = Table(f, dataframe=df)
        pt.show()

        # scrollbar = ttk.Scrollbar(root)
        # scrollbar.pack(side = RIGHT, fill=Y)
        
        # ListaSetor = ttk.Listbox(root, yscrollcommand = scrollbar.set, width = 60)
        # for linha in range(0,len(setores)):
        #     ListaSetor.insert(END, setores[linha])            
        
        # ListaSetor.pack(side = LEFT, fill = BOTH)
        # scrollbar.config(command= ListaSetor.yview)
        
        # labelResult.config(text = "Retorno Consulta")
    # if setores != None: 
    #     for setor in setores:
    #         print(setor)
    else:
        labelResult.config(text = "Setor não encontrado")

def checkfill(codigo, setor, codcoord):

    return codigo.get()=='' or codcoord.get()=='' or setor.get==''

def getColumnName():
    COLUMN_NAME = banco.QueryColumnSetor()
    colunas_tabela = []

    if COLUMN_NAME != None: 
        for i in COLUMN_NAME:
            colunas_tabela.append(i[3])
        return colunas_tabela
    else:
        return []