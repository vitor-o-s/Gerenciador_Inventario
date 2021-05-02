import banco
import tkinter as tk
from tkinter import *
from functools import partial




''' MÉTODOS IMPLEMENTADOS:

    - CadastroSetor() #Tela Cadastro
    - ConsultaSetor() #Tela Consulta
    - FuncaoButtonCadastro() #Botao tela Cadastro
    - FuncaoButtonConsulta() #Botao tela Consulta
    - checkfill() #Verifica se campos vazio


'''

""" LISTA CORREÇÃO:



"""

#####################################################################
############################ CADASTRO SETOR #########################
#####################################################################

def CadastroSetor():

    Setor = tk.Tk()
    Setor.geometry('400x300')
    Setor.title('Cadastro de Setores')
    lblCodigo = Label(Setor, text='Codigo do setor:')
    lblCodigo.grid(column=0, row=0)
    txtCodigo = Entry(Setor, width=10)
    txtCodigo.grid(column=1, row=0)
    lblNomeSetor = Label(Setor, text='Setor:')
    lblNomeSetor.grid(column=0, row=1)
    txtNomeSetor = Entry(Setor, width=30)
    txtNomeSetor.grid(column=1, row=1)
    lblCodigoCoordenador = Label(Setor, text='Código Coordenador:')
    lblCodigoCoordenador.grid(column=0, row=2)
    txtCodigoCoordenador = Entry(Setor, width=10)
    txtCodigoCoordenador.grid(column=1, row=2)


    labelResult = tk.Label(Setor)  
    labelResult.grid(row=4, column=1) 

    btnIncluir = Button(Setor, text='Incluir', command = partial(FuncaoButtonCadastro, 
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
    Setor.geometry('400x300')

    Setor.title('Consulte Setores')
    lblCodigo = Label(Setor, text='Codigo do setor:')
    lblCodigo.grid(column=0, row=0)
    txtCodigo = Entry(Setor, width=10)
    txtCodigo.grid(column=1, row=0)
    
    lblNomeSetor = Label(Setor, text='Setor:')
    lblNomeSetor.grid(column=0, row=1)
    txtNomeSetor = Entry(Setor, width=30)
    txtNomeSetor.grid(column=1, row=1)
    
    lblCodigoCoordenador = Label(Setor, text='Código Coordenador:')
    lblCodigoCoordenador.grid(column=0, row=2)
    txtCodigoCoordenador = Entry(Setor, width=10)
    txtCodigoCoordenador.grid(column=1, row=2)

    labelResult = tk.Label(Setor)  
    labelResult.grid(row=4, column=1) 

    btnIncluir = Button(Setor, text='Consultar', command = partial(FuncaoButtonConsulta, txtCodigo, txtNomeSetor,txtCodigoCoordenador, labelResult))
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

############################# FUNÃO BOTÃO CONSULTA #################################

####################################################################################
def FuncaoButtonConsulta(codigoSetor, setor, codcoord, labelResult):

    setores = banco.ConsultaSetor(codigoSetor.get(), setor.get(), codcoord.get(), labelResult)

    if setores != None:
        root = tk.Tk()
        root.geometry('400x300')
        root.title("Lista de Setores")
        


        scrollbar = Scrollbar(root)
        scrollbar.pack(side = RIGHT, fill=Y)
        
        ListaSetor = Listbox(root, yscrollcommand = scrollbar.set, width = 60)
        for linha in range(0,len(setores)):
            ListaSetor.insert(END, setores[linha])            
        
        ListaSetor.pack(side = LEFT, fill = BOTH)
        scrollbar.config(command= ListaSetor.yview)
        
        labelResult.config(text = "Retorno Consulta")
    # if setores != None: 
    #     for setor in setores:
    #         print(setor)
    else:
        labelResult.config(text = "Setor não encontrado")

def checkfill(codigo, setor, codcoord):

    return codigo.get()=='' or codcoord.get()=='' or setor.get==''
