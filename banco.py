import psycopg2


def salvarpessoa(codigo, nome, cargo, email):

    with psycopg2.connect(host="Localhost",database="mydb", user="postgres", password="123") as conn:

        with conn.cursor() as cur:
            #Example
            cur.execute("""
                        INSERT INTO PESSOA (codPessoa, nomeCompleto, email)
                        VALUES (%s, %s, %s);
                        """,
                        (int(codigo),str(nome), str(email)))
                        
        conn.commit()
