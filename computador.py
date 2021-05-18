from tkinter.constants import BOTH, END, LEFT, RIGHT, Y
import banco
import tkinter as tk
from tkinter import ttk, Label, Button, Entry, Menu, Toplevel, Scrollbar,Listbox,Frame
from functools import partial
import pandas as pd
from pandastable import Table

''' MÉTODOS IMPLEMENTADOS:
    
    - CadastroComputador() #Tela Cadastro
    - ConsultaComputador() #Tela Consulta
    - FuncaoButtonCadastro() #Botao tela Cadastro
    - FuncaoButtonConsulta() #Botao tela Consulta
    - checkfill #Verifica se campos vazio


    


'''



##############################################################################################################################

########################################## CADASTRO COMPUTADOR ###################################################################

##############################################################################################################################

def CadastroComputador():

    computador = tk.Tk()
    style = ttk.Style(computador)
    style.theme_use('clam')
    computador.geometry('800x600')
    computador.title("Cadastro de Computador")
    row = 0
    lblTipoComputador = ttk.Label(computador, text='Tipo:')
    lblTipoComputador.grid(column=0, row=row)
    txtTipoComputador = ttk.Entry(computador, width=50)
    txtTipoComputador.grid(column=1, row=row)
    row += 1

    lblModeloMB = ttk.Label(computador, text='Modelo MB:')
    lblModeloMB.grid(column=0, row=row)
    txtModeloMB = ttk.Entry(computador, width=50)
    txtModeloMB.grid(column=1, row=row)
    row += 1

    lblNumeroSerie = ttk.Label(computador, text='numero de serie:')
    lblNumeroSerie.grid(column=0, row=row)
    txtNumeroSerie = ttk.Entry(computador, width=50)
    txtNumeroSerie.grid(column=1, row=row)
    row += 1

    lblModeloNotebook = ttk.Label(computador, text='Modelo Notebook:')
    lblModeloNotebook.grid(column=0, row=row)
    txtModeloNotebook = ttk.Entry(computador, width=50)
    txtModeloNotebook.grid(column=1, row=row)
    row += 1

    lblModeloChipset = ttk.Label(computador, text='Modelo Chipset:')
    lblModeloChipset.grid(column=0, row=row)
    txtModeloChipset = ttk.Entry(computador, width=50)
    txtModeloChipset.grid(column=1, row=row)
    row += 1

    lblProcessador = ttk.Label(computador, text='Processador:')
    lblProcessador.grid(column=0, row=row)
    txtProcessador = ttk.Entry(computador, width=50)
    txtProcessador.grid(column=1, row=row)
    row += 1

    lblRam = ttk.Label(computador, text='Ram:')
    lblRam.grid(column=0, row=row)
    txtRam = ttk.Entry(computador, width=50)
    txtRam.grid(column=1, row=row)
    row += 1

    lblRom = ttk.Label(computador, text='Rom:')
    lblRom.grid(column=0, row=row)
    txtRom = ttk.Entry(computador, width=50)
    txtRom.grid(column=1, row=row)
    row += 1

    lblCodigoSetor = ttk.Label(computador, text='Código do Setor:')
    lblCodigoSetor.grid(column=0, row=row)
    txtCodigoSetor = ttk.Entry(computador, width=50)
    txtCodigoSetor.grid(column=1, row=row)
    row += 1

    lblmacETH = ttk.Label(computador, text='macETH:')
    lblmacETH.grid(column=0,row=row)
    txtmacETH = ttk.Entry(computador,width=50)
    txtmacETH.grid(column=1,row=row)
    row += 1

    lblmacWLAN = ttk.Label(computador, text='macWLAN:')
    lblmacWLAN.grid(column=0,row=row)
    txtmacWLAN = ttk.Entry(computador,width=50)
    txtmacWLAN.grid(column=1,row=row)
    row += 1

    '''
	macETH MACADDR NOT NULL, - criado
	macWLAN MACADDR NOT NULL, - criado
	tipoComputador VARCHAR(8), - ja tem
	modeloMB VARCHAR(30), - ja tem 
	numeroSerie VARCHAR(30), -  ja tem 
	modeloNotebook VARCHAR(30), - ja tem
	modeloChipset VARCHAR(30), - ja tem 
	processador VARCHAR(30), - ja tem
	ram VARCHAR(50), - ja tem
	rom VARCHAR(50), - ja tem
	codSetor INTEGER, - lista de setores disponiveis ? 
    '''
    
    labelResult = ttk.Label(computador)  
    labelResult.grid(row=row, column=1) 
    row += 1

    btnIncluir = ttk.Button(computador, text='Incluir', 
                        command=partial(FuncaoButtonCadastro,
                                        txtmacETH,
                                        txtmacWLAN,
                                        txtTipoComputador, 
                                        txtModeloMB, 
                                        txtNumeroSerie, 
                                        txtModeloNotebook, 
                                        txtModeloChipset, 
                                        txtProcessador, 
                                        txtRam,txtRom, 
                                        labelResult))
    btnIncluir.grid(column=1, row=row)


##############################################################################################################################

########################################## CONSULTA COMPUTADOR ###################################################################

##############################################################################################################################


def ConsultaComputador():

    computador = tk.Tk()
    style = ttk.Style(computador)
    style.theme_use('clam')
    computador.geometry('800x600')
    computador.title("Cadastro de Computador")
    row = 0
    lblTipoComputador = ttk.Label(computador, text='Tipo:')
    lblTipoComputador.grid(column=0, row=row)
    txtTipoComputador = ttk.Entry(computador, width=50)
    txtTipoComputador.grid(column=1, row=row)
    row += 1

    lblModeloNotebook = ttk.Label(computador, text='Modelo Notebook:')
    lblModeloNotebook.grid(column=0, row=row)
    txtModeloNotebook = ttk.Entry(computador, width=50)
    txtModeloNotebook.grid(column=1, row=row)
    row += 1

    lblProcessador = ttk.Label(computador, text='Processador:')
    lblProcessador.grid(column=0, row=row)
    txtProcessador = ttk.Entry(computador, width=50)
    txtProcessador.grid(column=1, row=row)
    row += 1


    lblmacETH = ttk.Label(computador, text='macETH:')
    lblmacETH.grid(column=0,row=row)
    txtmacETH = ttk.Entry(computador,width=50)
    txtmacETH.grid(column=1,row=row)
    row += 1

    labelResult = ttk.Label(computador) 
    btnIncluir = ttk.Button(computador, text='Consultar', 
                        command=partial(FuncaoButtonConsulta,
                                        txtmacETH,
                                        txtTipoComputador, 
                                        txtModeloNotebook,
                                        txtProcessador, 
                                        labelResult))
    btnIncluir.grid(column=1, row=row)   
 
    row += 1


    
    labelResult.grid(row=row, column=1)

##############################################################################################################################
########################################## FUNÇÃO BOTÃO CADASTRA COMPUTADOR ###################################################################
##############################################################################################################################


def FuncaoButtonCadastro(macETH, macWLAN, tipo, modeloMB, numserie, modelonot, modelochipset, processador, ram, rom, labelResult):

    if checkfill(macETH, macWLAN, tipo, modeloMB, numserie, modelonot, modelochipset, processador, ram, rom):
        labelResult.config(text="Um dos campos não foi preenchido. Favor verificar")

    else:
        resultado = banco.salvarcomputador(macETH.get(),
                                            macWLAN.get(),
                                            tipo.get(),
                                            modeloMB.get(),
                                            numserie.get(),
                                            modelonot.get(),
                                            modelochipset.get(),
                                            processador.get(),
                                            ram.get(),
                                            rom.get(),
                                            labelResult)
        if resultado:

            labelResult.config(text="Computador cadastrado com sucesso!")
        else:
            labelResult.config(text="Computador já existe na tabela")
        
##############################################################################################################################
########################################## FUNÇÃO BOTÃO CONSULTA COMPUTADOR ################################################
##############################################################################################################################

def FuncaoButtonConsulta(macETH, tipo, modelonot, processador, labelResult):
    
    computadores = banco.ConsultaComputador(macETH.get(), tipo.get(), modelonot.get(), processador.get(), labelResult)

    colunas = getColumnName()

    listaComputadores = []
    print(computadores)
    for i in range(0,len(computadores)):
        listaComputadores.append(list(computadores[i]))

    df = pd.DataFrame(listaComputadores, columns=colunas)



    if computadores != None:
        root = tk.Tk()
        style = ttk.Style(root)
        style.theme_use('clam')
        root.geometry('800x600')
        root.title("Lista de computadores")

        f = Frame(root)
        f.pack(fill=BOTH,expand=1)
        pt = Table(f, dataframe=df)
        pt.show()

        # scrollbar = Scrollbar(root)
        # scrollbar.pack(side = RIGHT, fill=Y)
        
        # ListaComputadores = Listbox(root, yscrollcommand = scrollbar.set, width = 60)
        # for linha in range(0,len(computadores)):
        #     ListaComputadores.insert(END, computadores[linha])            
        
        # ListaComputadores.pack(side = LEFT, fill = BOTH)
        # scrollbar.config(command= ListaComputadores.yview)
        
        # labelResult.config(text = "Retorno Consulta")

    else:
        labelResult.config(text = "Empresa não encontrado")      

def checkfill(macETH, macWLAN, tipo, modeloMB, numserie, modelonot, modelochipset, processador, ram, rom):

    return (macETH.get()=='' or macWLAN.get()==''
            or tipo.get()=='' or modeloMB.get()=='' 
            or numserie.get()=='' or modelonot.get()==''
            or modelochipset.get()==''or processador.get()==''
            or ram.get()=='' or rom.get()=='')

def getColumnName():
    COLUMN_NAME = banco.QueryColumnComputador()
    colunas_tabela = []

    if COLUMN_NAME != None: 
        for i in COLUMN_NAME:
            colunas_tabela.append(i[3])
        return colunas_tabela
    else:
        return []