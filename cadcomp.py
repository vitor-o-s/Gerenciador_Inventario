import tkinter as tk
from tkinter import Label, Entry, Button

def CadastroComputador():
    computador = tk.Tk()
    computador.geometry('400x300')
    computador.title("Cadastro de Computador")
    lblTipoComputador = Label(computaodr, text='Tipo:')
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
    txtRom = Entry(Pessoa, width=50)
    txtRom.grid(column=1, row=7)
    lblCodigoSetor = Label(computador, text='Código do Setor:')
    lblCodigoSetor.grid(column=0, row=8)
    txtCodigoSetor = Entry(Pessoa, width=50)
    txtCodigoSetor.grid(column=1, row=8)
    

    btnIncluir = Button(computador, text='Incluir')
    btnIncluir.grid(column=2, row=6)