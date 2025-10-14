import pandas as pd

df = pd.read_csv('dados/dataset.csv')
media = df['valor'].mean()
print(f'Média dos valores: {media}')
