nome = "matheus@ felipin yokoyama"
teste = nome.split(' ')
nome_completo = ''


for i in teste:
    nome_completo = nome_completo + str.upper(list(i)[0]) 
    nome_completo = nome_completo + str.lower(i[1:])
if str.isalpha(nome_completo):
    print("OK")
else:
    print("NOK")