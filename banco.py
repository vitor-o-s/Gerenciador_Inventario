import psycopg2
pswd = 'a8ee2d0d3e8741fa884c1c190aa2f384d53a96b5fe96443eac9863c261822cbc'
host = 'ec2-54-167-152-185.compute-1.amazonaws.com'
user = 'nkqrevofvmcinl'
db   = 'dbvmtp12eqm8g8'
port = 5432

def salvarpessoa(nome, cargo, email, labelResult):
    
    conn = psycopg2.connect(host=host,database=db, user=user, password=pswd)
    
    try:
        if conn is not None:
            print('Connection established to PostgreSQL.')
            with conn.cursor() as cur:

                ###################################################################################
                ####### BUSCA NO BANCO INFORMAÇOES SE JÁ EXISTE USUARIO CADASTRADO ################
                ###################################################################################
                
                if(checkEmail(email)==1):
                    if(mask(email) == 1):
                        print("Cadastrando usuario")
                        ############## CORRIGIR QUERY PARA INSERIR USUARIO
                        cur.execute("""
                                    INSERT INTO PESSOA (nomeCompleto, email, cargo)
                                    VALUES (%s, %s, %s);
                                    """,
                                    (str(nome), str(email),str(cargo)))
                        # conn.commit() # commit para atualizar o banco 
                        return 1        
                    else:
                        print("Dominio email invalido")
                        return -1
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

def mask(s):
    lo = s.find('@')
    if checkDomain(s, lo) == 1:
        # print("Email valido")
        return 1
    else:
        # print("email invalido")
        return -1

def checkDomain(s, lo):
    dominio_email = s[lo:]
    if dominio_email == '@empresa.com.br':
        return 1
    else:
        return -1


##################################################
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