import pandas as pd

df = pd.read_json("dados.json")

df2 = df.loc[df['valor'] > 0]

df2 = df2.reset_index()
df2 = df2.drop('index', axis=1)

menor_faturamento = (df2['valor'].min())
maior_faturamento = (df2['valor'].max())

media = df2['valor'].mean()

dias = 0
for i in df2['valor']:
    if i > media:
        dias += 1


print(f'Maior faturamento no mês: R$ {round(maior_faturamento, 2)}')
print(f'Menor faturamento no mês: R$ {round(menor_faturamento, 2)}')
print(f'Em {dias} dias no mês o faturamento superou a media mensal de: R$ {round(media, 2)}')
