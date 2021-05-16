import psycopg2
pswd = 'a8ee2d0d3e8741fa884c1c190aa2f384d53a96b5fe96443eac9863c261822cbc'
host = 'ec2-54-167-152-185.compute-1.amazonaws.com'
user = 'nkqrevofvmcinl'
db   = 'dbvmtp12eqm8g8'
port = 5432



'''
    Métodos implementados:

    - salvarpessoa()
    - ConsultaPessoa()
    - salvarsetor()
    - salvarempresa()
    - salvarcomputador
    - checkEmail()
    - checkSetor()
    - checkEmpresa()
    - checkComputador()




'''
########################################################################
######################## INCLUSAO PESSOA ###############################
########################################################################

def salvarpessoa(nome, email, labelResult):
    
    conn = psycopg2.connect(host=host,database=db, user=user, password=pswd)
    
    try:
        if conn is not None:
            print('Connection established to PostgreSQL.')
            with conn.cursor() as cur:

                ###################################################################################
                ####### BUSCA NO BANCO INFORMAÇOES SE JÁ EXISTE USUARIO CADASTRADO ################
                ###################################################################################
                
                if(checkEmail(email)==1):
                        print("Cadastrando usuario")
                        cur.execute("""
                                    INSERT INTO PESSOA (nomeCompleto, email)
                                    VALUES (%s, %s);
                                    """,
                                    (str(nome), str(email)))
                        conn.commit() # commit para atualizar o banco 
                        return 1        
                else:
                    print("Email cadastrado")
 
                    return 0
        else:
            print('Connection not established to PostgreSQL.')
            
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    finally:
        if conn is not None:
            conn.close()
            print('Finally, connection closed.')

################################################################
######################## CONSULTA PESSOA #######################
################################################################

def ConsultaPessoa(nome, email, labelResult):

    conn = psycopg2.connect(host=host,database=db, user=user, password=pswd)
    try:
        if conn is not None:
            print('Connection established to PostgreSQL.')
            with conn.cursor() as cur:
                
                if (nome=='' and email ==''):
                    cur.execute("""
                                SELECT * FROM PESSOA
                                """)
                elif(nome!='' and email == ''):
                    cur.execute("""
                                SELECT * FROM PESSOA
                                WHERE 1=1
                                AND nomeCompleto LIKE '%s%%';
                                """ % nome)

                elif(nome == '' and email != ''):
                    cur.execute("""
                                SELECT * FROM PESSOA
                                WHERE 1=1
                                AND email LIKE LOWER('%s%%');
                                """ % (email))
                else:
                    cur.execute("""
                                SELECT * FROM PESSOA
                                WHERE 1=1
                                AND nomeCompleto LIKE '%s%%'
                                AND email LIKE LOWER('%s%%')
                                """ % (nome, email))
                        # conn.commit() # commit para atualizar o banco 
                registros = cur.fetchall()

                return registros
        else:
            print('Connection not established to PostgreSQL.')
            
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    finally:
        if conn is not None:
            conn.close()
            print('Finally, connection closed.')

    ### RETORNA TODAS COLUNAS DA TABELA
def QueryColumnPessoa():
    conn = psycopg2.connect(host=host,database=db, user=user, password=pswd)
    try:
        if conn is not None:
            print('Connection established to PostgreSQL.')
            with conn.cursor() as cur:
                cur.execute(""" 
                            SELECT *
                            FROM INFORMATION_SCHEMA.COLUMNS
                            WHERE TABLE_NAME = 'pessoa'
                            """)
                registros = cur.fetchall()
            return registros
        else:
            print('Connection not established to PostgreSQL.')
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    finally:
        if conn is not None:
            conn.close()
            print('Finally, connection closed.')

################################################################
######################## INCLUIR SETOR   #######################
################################################################

def salvarsetor(codigo, setor, codcoord, labelResult):
    conn = psycopg2.connect(host=host,database=db, user=user, password=pswd)
    
    try:        
        if conn is not None:
            print('Connection established to PostgreSQL.')
            with conn.cursor() as cur:
                
                if(checkSetor(setor)==1):
                        print("Cadastrando Computador")
                        cur.execute("""
                                    INSERT INTO SETOR (codEmpresa, codCoordenador, nomeSetor)
                                    VALUES (%s, %s);
                                    """,
                                    (str(codigo), str(codcoord), str(setor)))
                        # conn.commit() # commit para atualizar o banco 
                        return 1        
                else:
                    print("Setor esta cadastrado no sistema") 
                    return 0

        else:
            print('Connection not established to PostgreSQL.')
            
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    finally:
        if conn is not None:
            conn.close()
            print('Finally, connection closed.')



def ConsultaSetor(codigoSetor, setor, codcoord, labelResult):

    conn = psycopg2.connect(host=host,database=db, user=user, password=pswd)
    try:
        if conn is not None:
            print('Connection established to PostgreSQL.')
            with conn.cursor() as cur:
                
                if (setor=='' and codigoSetor ==''):
                    cur.execute("""
                                SELECT * FROM SETOR
                                """)
                ### Terminar de colocar condições para consulta


                        # conn.commit() # commit para atualizar o banco 
                setores = cur.fetchall()

                return setores
        else:
            print('Connection not established to PostgreSQL.')
            
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    finally:
        if conn is not None:
            conn.close()
            print('Finally, connection closed.')


################################################################
######################## INCLUIR EMPRESA #######################
################################################################


def salvarempresa(codigo, nomeempresa, tel, codresp, labelResult):
    conn = psycopg2.connect(host=host,database=db, user=user, password=pswd)
    
    try:        
        if conn is not None:
            print('Connection established to PostgreSQL.')
            with conn.cursor() as cur:
                
                if(checkEmpresa(nomeempresa)==1):
                        print("Cadastrando Computador")
                        cur.execute("""
                                    INSERT INTO EMPRESA (codEmpresa, nomeEmpresa, telefone)
                                    VALUES (%s, %s, %s);
                                    """,
                                    (str(codigo), str(nomeempresa), str(tel)))
                        # conn.commit() # commit para atualizar o banco 
                        return 1        
                else:
                    print("Computador cadastrado")
 
                    return 0
            
            
        else:
            print('Connection not established to PostgreSQL.')
            
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    finally:
        if conn is not None:
            conn.close()
            print('Finally, connection closed.')

def ConsultaEmpresa(codigo, nomeempresa, tel, codresp, labelResult):

    conn = psycopg2.connect(host=host,database=db, user=user, password=pswd)
    try:
        if conn is not None:
            print('Connection established to PostgreSQL.')
            with conn.cursor() as cur:
                
                if (nomeempresa=='' and codresp ==''):
                    cur.execute("""
                                SELECT * FROM EMPRESA
                                """)
                ### Terminar de colocar condições para consulta


                        # conn.commit() # commit para atualizar o banco 
                empresas = cur.fetchall()

                return empresas
        else:
            print('Connection not established to PostgreSQL.')
            
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    finally:
        if conn is not None:
            conn.close()
            print('Finally, connection closed.')


################################################################
######################## INCLUIR COMPUTADOR ####################
################################################################


def salvarcomputador(macETH, macWLAN, tipo, modeloMB, numserie, modelonot, modelochipset, processador, ram, rom, labelResult):

    conn = psycopg2.connect(host=host,database=db, user=user, password=pswd)
    
    try:        
        if conn is not None:
            print('Connection established to PostgreSQL.')
            with conn.cursor() as cur:
                
                if(checkComputador(macETH,macWLAN)==1):
                        print("Cadastrando Computador")
                        cur.execute("""
                                    INSERT INTO COMPUTADOR (macETH,
                                                            macWLAN,
                                                            tipoComputador,
                                                            modeloMB,
                                                            numeroSerie,
                                                            modeloNotebook,
                                                            modeloChipset,
                                                            processador,
                                                            ram,
                                                            rom)
                                    VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s);
                                    """,
                                    (str(macETH),
                                     str(macWLAN),
                                     str(tipo),
                                     str(modeloMB),
                                     str(numserie),
                                     str(modelonot),
                                     str(modelochipset),
                                     str(processador),
                                     str(ram),
                                     str(rom) ))
                        # conn.commit() # commit para atualizar o banco 
                        return 1        
                else:
                    print("Computador cadastrado")
 
                    return 0
            
            
        else:
            print('Connection not established to PostgreSQL.')
            
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    finally:
        if conn is not None:
            conn.close()
            print('Finally, connection closed.')


def ConsultaComputador(macETH, macWLAN, tipo, modeloMB, numserie, modelonot, modelochipset, processador, ram, rom, labelResult):

    conn = psycopg2.connect(host=host,database=db, user=user, password=pswd)
    try:
        if conn is not None:
            print('Connection established to PostgreSQL.')
            with conn.cursor() as cur:
                
                if (tipo=='' and modelonot ==''):
                    cur.execute("""
                                SELECT * FROM COMPUTADOR
                                """)
                ### Terminar de colocar condições para consulta


                        # conn.commit() # commit para atualizar o banco 
                computadores = cur.fetchall()

                return computadores
        else:
            print('Connection not established to PostgreSQL.')
            
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    finally:
        if conn is not None:
            conn.close()
            print('Finally, connection closed.')


def checkEmail(email):
    conn = psycopg2.connect(host=host,database=db, user=user, password=pswd)
    cur2 = conn.cursor()
    cur2.execute("""
            SELECT nomeCompleto, email
            FROM PESSOA
            WHERE 1=1
            AND email = '"""+str(email)+"""'
            """)
    #print(cur2.fetchall())
    if cur2.fetchall() == []:
        cur2.close()
        return 1
    else:
        # print("Existe usuario cadastrado com este e-mail")
        cur2.close()
        return -1 

#Testar
def checkSetor(setor):

    conn = psycopg2.connect(host=host,database=db, user=user, password=pswd)
    cur2 = conn.cursor()
    # cur2.execute("""
    #         SELECT nomeSetor
    #         FROM SETOR
    #         WHERE 1=1 
    #         AND nomeSetor LIKE LOWER('%s%%')   
    #         """ % (setor))
    cur2.execute(""" 
                SELECT *
                FROM INFORMATION_SCHEMA.COLUMNS
                WHERE TABLE_NAME = 'setor'
                """)
    # cur2.execute("""
    #         SELECT nomeSetor
    #         FROM SETOR
    #         WHERE 1=1 
    #         AND nomeSetor  
    #         """)
    print(cur2.fetchall())

    if cur2.fetchall() == []:
        cur2.close()
        return 1
    else:
        cur2.close()
        return -1

#Testar
def checkEmpresa(empresa):

    conn = psycopg2.connect(host=host,database=db, user=user, password=pswd)
    cur2 = conn.cursor()
    cur2.execute("""
            SELECT nomeEmpresa
            FROM EMPRESA
            WHERE 1=1 
            AND nomeEmpresa =  '"""+str(empresa)+"""'   
            """)
    if cur2.fetchall() == []:
        cur2.close()
        return 1
    else:
        # print("Existe usuario cadastrado com este e-mail")
        cur2.close()
        return -1

#Testar
def checkComputador(macETH, macWLAN):
    conn = psycopg2.connect(host=host,database=db, user=user, password=pswd)
    cur2 = conn.cursor()
    cur2.execute("""
            SELECT macETH,
            FROM COMPUTADOR
            WHERE 1=1 
            AND macETH =  '"""+str(macETH)+"""'   
            """)
    if cur2.fetchall() == []:
        cur2.close()
        return 1
    else:
        # print("Existe usuario cadastrado com este e-mail")
        cur2.close()
        return -1




#RETORNA TODOS USUARIOS
#cur.execute("SELECT * FROM PESSOA ;")

#### LINHA PARA EXCLUIR USUARIOS SEM NOME
# cur.execute("DELETE FROM PESSOA WHERE nomeCompleto = ''")
# linhas_deletadas = cur.rowcount
#return linhas_deletadas


############### Retorna usuario do e-mail inserido
# cur.execute("""
#             SELECT nomeCompleto, email
#             FROM PESSOA
#             WHERE 1=1
#             AND email = '"""+str(email)+"""'        
#             """)
# result = cur.fetchall() 
# return result