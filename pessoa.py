import tkinter as tk
from tkinter import *
from functools import partial
import banco
import time
#import TkTreectrl as treectrl

''' MÉTODOS IMPLEMENTADOS:

    - CadastroPessoa() #Tela Cadastro
    - ConsultaPessoa() #Tela Consulta
    - FuncaoButtonCadastro() #Botao tela Cadastro
    - FuncaoButtonConsulta() #Botao tela Consulta
    - checkfill() #Verifica se campos vazio
    - mask() #Verifica se mascara email valida
    - checkDomain() #Verifica se domínio email válido
    


'''

"""     LISTA DE CORREÇÃO
    
    FUNCAO BOTAO CONSULTA:
    - TERMINAR TELA DE CONSULTA 
    --> AO CONSULTAR SEM PREENCHER NENHUM PARAMETRO DEVE TRAZER TODAS PESSOAS 
    --> LISTAR NOME DA COLUNA E SEUS RESPECTIVOS VALORES (Ex: https://stackoverflow.com/questions/5286093/display-listbox-with-columns-using-tkinter)
    
    - CRIAR UMA NOVA COLUNA "CARGO" PARA OS USUÁRIOS (Pode ser integer ou sting) 
    
"""
##############################################################################################################################

########################################## CADASTRO PESSOA ###################################################################

##############################################################################################################################

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

    btnIncluir = Button(Pessoa, text='Incluir', command = partial(FuncaoButtonCadastro, txtNomePessoa, txtEmail,labelResult))
    btnIncluir.grid(column=1, row=6)


###############################################################################################################################

###################################################### CONSULTA PESSOA ########################################################

###############################################################################################################################

    '''
    A função deve conseguir consultar pessoas pelo nome, pelo email ou pelos 2.
    * Caso não seja inserido nenhum informação e clicado no botão "Consultar" deve retornar a lista de todos.
    ** A consulta sem preenchumento dos parâmetros só deve ser permitido enquanto não haver muitos registros de pessoas no sistema
    '''

def ConsultaPessoa():

    Pessoa = tk.Tk()
    
    Pessoa.geometry('400x300')
    Pessoa.title("Consultando Pessoas")
    


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

    btnIncluir = Button(Pessoa, text='Consultar', command = partial(FuncaoButtonConsulta, 
                                                                  txtNomePessoa, 
                                                                  txtEmail, labelResult))
    btnIncluir.grid(column=1, row=6)


##############################################################################################################################
##############
########################################## BOTÃO DE CADASTRO #################################################################
##############
##############################################################################################################################

def FuncaoButtonCadastro(nome, email,labelResult):

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
            labelResult.config(text="Dominio email invalido")
            return 


##############################################################################################################################
##############
########################################## BOTÃO DE CONSULTA #################################################################
##############
##############################################################################################################################


def FuncaoButtonConsulta(nome, email, labelResult):
    pessoas = banco.ConsultaPessoa(nome.get(), email.get(), labelResult)

    #colunas = getColumnName()
    if pessoas != None:
        root = tk.Tk()
        root.geometry('400x300')
        root.title("Lista de Pessoas")
        
        ### TESTE
        #ListaPessoa = treectrl.MultiListbox(root)
        # ListaPessoa.pack(side='top', fill='both', expand=1)
        # tk.Button(root, text='Close', command=root.quit).pack(side='top', pady=5)
        # ListaPessoa.focus_set()   
        # ListaPessoa.configure(selectcmd=select_cmd, selectmode='extended')
        # ListaPessoa.config(columns=colunas)


        scrollbar = Scrollbar(root)
        scrollbar.pack(side = RIGHT, fill=Y)
        
        ListaPessoa = Listbox(root, yscrollcommand = scrollbar.set, width = 60)
        for linha in range(0,len(pessoas)):
            ListaPessoa.insert(END, pessoas[linha])            
        
        ListaPessoa.pack(side = LEFT, fill = BOTH)
        scrollbar.config(command= ListaPessoa.yview)
        
        labelResult.config(text= "resultado encontrado")
    else:
        labelResult.config(text= "resultado não encontrado")


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


def checkfill(nome, email):

    return nome.get()=='' or email.get()=='' 

def mask(s):
    lo = s.find('@')
    return checkDomain(s, lo) == 1

def checkDomain(s, lo):
    dominio_email = s[lo:]
    return dominio_email == '@empresa.com.br'