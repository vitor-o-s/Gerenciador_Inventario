import setor, pessoa, computador, empresa
import tkinter as tk
from tkinter import  ttk, Menu

def clickedpessoa():
    return pessoa.CadastroPessoa()

def clickedsetor():
    return setor.CadastroSetor()

def clickedempresa():
    return empresa.CadastroEmpresa()

def clickedcomputador():
    return computador.CadastroComputador()
    

def ConsultaPessoa():
    return pessoa.ConsultaPessoa()

def ConsultaSetor():
    return setor.ConsultaSetor()

def ConsultaEmpresa():
    return empresa.ConsultaEmpresa()

def ConsultaComputador():
    return computador.ConsultaComputador()


##############################################################################################################################

########################################## CRIAÇÃO BOTÃO DE CADASTRO ########################################################

##############################################################################################################################

def BotaoCadastro(menu):
    #Cria o botão de cadastro e inclui as opções 
    itemCadastro = Menu(menu)
    itemCadastro.add_command(label='Pessoa', command=clickedpessoa)
    itemCadastro.add_separator()
    itemCadastro.add_command(label='Setor', command=clickedsetor)
    itemCadastro.add_separator()
    itemCadastro.add_command(label='Empresa', command=clickedempresa)
    itemCadastro.add_separator()
    itemCadastro.add_command(label='Computador', command=clickedcomputador)
    itemCadastro.add_separator()
    itemCadastro.add_command(label='Sair', command=quit)
    return itemCadastro

##############################################################################################################################

########################################## CRIAÇÃO BOTÃO DE CONSULTA ########################################################

##############################################################################################################################

def BotaoConsulta(menu):
    itemConsulta = Menu(menu)

    itemConsulta.add_command(label='Pessoa', command=ConsultaPessoa)
    itemConsulta.add_separator()    
    itemConsulta.add_command(label='Setor', command=ConsultaSetor)

    itemConsulta.add_separator()
    itemConsulta.add_command(label='Empresa', command=ConsultaEmpresa)
    itemConsulta.add_separator()
    itemConsulta.add_command(label='Computador', command=ConsultaComputador)


    return itemConsulta 







if __name__ == "__main__":

    main = tk.Tk()
    style = ttk.Style(main)
    style.theme_use('clam')
    main.geometry('800x600')
    main.title("SistemaInventário")
    lbl = ttk.Label(main, text='Seja bem vindo', font='courier 15')
    lbl.grid(column=0, row=0)

    menubar = Menu(main)
    # dentro da barra de menu cria a opção do Cadastro (botão)
    itemCadastro = BotaoCadastro(menubar)
    itemCadastro.add_separator()

    # dentro da barra de menu cria a opção de Consulta (botão)
    itemConsulta = BotaoConsulta(menubar)
    itemConsulta.add_separator()

    # Adiciona 
    menubar.add_cascade(label='Cadastro', menu=itemCadastro)
    menubar.add_cascade(label='Consulta', menu=itemConsulta)

    main.config(menu=menubar)
    main.mainloop()

#Gustavo Martins de Souza
#gustavos@empresa.com.br