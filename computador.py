import banco
import tkinter as tk
from tkinter import Label, Entry, Button
from functools import partial


def CadastroComputador():

    computador = tk.Tk()
    computador.geometry('400x300')
    computador.title("Cadastro de Computador")

    lblTipoComputador = Label(computador, text='Tipo:')
    lblTipoComputador.grid(column=0, row=0)
    txtTipoComputador = Entry(computador, width=50)
    txtTipoComputador.grid(column=1, row=0)
    lblModeloMB = Label(computador, text='Modelo MB:')
    lblModeloMB.grid(column=0, row=1)
    txtModeloMB = Entry(computador, width=50)
    txtModeloMB.grid(column=1, row=1)
    lblNumeroSerie = Label(computador, text='numero de serie:')
    lblNumeroSerie.grid(column=0, row=2)
    txtNumeroSerie = Entry(computador, width=50)
    txtNumeroSerie.grid(column=1, row=2)
    lblModeloNotebook = Label(computador, text='Modelo Notebook:')
    lblModeloNotebook.grid(column=0, row=3)
    txtModeloNotebook = Entry(computador, width=50)
    txtModeloNotebook.grid(column=1, row=3)
    lblModeloChipset = Label(computador, text='Modelo Chipset:')
    lblModeloChipset.grid(column=0, row=4)
    txtModeloChipset = Entry(computador, width=50)
    txtModeloChipset.grid(column=1, row=4)
    lblProcessador = Label(computador, text='Processador:')
    lblProcessador.grid(column=0, row=5)
    txtProcessador = Entry(computador, width=50)
    txtProcessador.grid(column=1, row=5)
    lblRam = Label(computador, text='Ram:')
    lblRam.grid(column=0, row=6)
    txtRam = Entry(computador, width=50)
    txtRam.grid(column=1, row=6)
    lblRom = Label(computador, text='Rom:')
    lblRom.grid(column=0, row=7)
    txtRom = Entry(computador, width=50)
    txtRom.grid(column=1, row=7)
    lblCodigoSetor = Label(computador, text='Código do Setor:')
    lblCodigoSetor.grid(column=0, row=8)
    txtCodigoSetor = Entry(computador, width=50)
    txtCodigoSetor.grid(column=1, row=8)
    lblmacETH = Label(computador, text='macETH:')
    lblmacETH.grid(column=0,row=9)
    txtmacETH = Entry(computador,width=50)
    txtmacETH.grid(column=1,row=9)
    lblmacWLAN = Label(computador, text='macWLAN:')
    lblmacWLAN.grid(column=0,row=10)
    txtmacWLAN = Entry(computador,width=50)
    txtmacWLAN.grid(column=1,row=10)

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
    
    labelResult = tk.Label(computador)  
    labelResult.grid(row=7, column=2) 

    btnIncluir = Button(computador, text='Incluir', 
                        command=partial(FuncaoButton,
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
    btnIncluir.grid(column=2, row=6)

def FuncaoButton(macETH, macWLAN, tipo, modeloMB, numserie, modelonot, modelochipset, processador, ram, rom, labelResult):

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
        

def checkfill(macETH, macWLAN, tipo, modeloMB, numserie, modelonot, modelochipset, processador, ram, rom):

    return (macETH.get()=='' or macWLAN.get()==''
            or tipo.get()=='' or modeloMB.get()=='' 
            or numserie.get()=='' or modelonot.get()==''
            or modelochipset.get()==''or processador.get()==''
            or ram.get()=='' or rom.get()=='')