
dados = [ ['SP', 67836.43], ['RJ', 36678.66], ['MG', 29229.88], ['ES', 27165.48], ['Outros', 19849.53] ]

total_faturamento = 0

i = 0
while i < len(dados):
    total_faturamento += dados[i][1]
    i+=1

i = 0
while i < len(dados):
    p = round((dados[i][1] / total_faturamento) * 100, 2)
    dados[i].append(p)
    i += 1

print(f'Faturamento total mensal: R$ {total_faturamento}')
print(f'Representação de cada estado: ')
n = 0
for i in dados:
    print(f'{dados[n][0]} : {dados[n][2]}%')
    n += 1