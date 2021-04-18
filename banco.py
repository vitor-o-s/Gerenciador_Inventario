import psycopg2
pswd = 'e08769fa9d15c60f3f5c20446c21e804c7242e853e06a05e1d21068a607a379f'
host = 'ec2-34-233-0-64.compute-1.amazonaws.com'
user = 'ozuqxrhmnofbkl'
db   = 'd3v409sdpeglku'


def salvarpessoa(nome, cargo, email):
    
    conn = psycopg2.connect(host=host,database=db, user=user, password=pswd)
    
    try:
        if conn is not None:
            print('Connection established to PostgreSQL.')
            with conn.cursor() as cur:
                #Example
                # cur.execute("""
                #             INSERT INTO PESSOA (nomeCompleto, email)
                #             VALUES (%s, %s, %s);
                #             """,
                #             (str(nome), str(email)))

                cur.execute("SELECT * FROM PESSOA")
                cur.fetchone()            
            conn.commit()
        else:
            print('Connection not established to PostgreSQL.')
            
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    finally:
        if conn is not None:
            conn.close()
            print('Finally, connection closed.')


