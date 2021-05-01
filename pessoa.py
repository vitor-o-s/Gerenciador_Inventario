import tkinter as tk
from tkinter import Label, Entry, Button
from functools import partial
import banco


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

    btnIncluir = Button(Pessoa, text='Incluir', command = partial(FuncaoButtonConsulta, 
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
    labelResult.config(text = "Consultando Pessoa")




def checkfill(nome, email):

    return nome.get()=='' or email.get()=='' 

def mask(s):
    lo = s.find('@')
    return checkDomain(s, lo) == 1

def checkDomain(s, lo):
    dominio_email = s[lo:]
    return dominio_email == '@empresa.com.br'