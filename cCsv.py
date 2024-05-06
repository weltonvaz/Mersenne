import pandas as pd

# Criando um DataFrame com os seus dados
data = {
    'numero': [2, 3, 4, 5, 6, 7, 8, 9, 10],
    'saida': [2, 2, 3, 2, 4, 2, 4, 3, 4]
}
df = pd.DataFrame(data)

# Salvando o DataFrame como um arquivo CSV
df.to_csv('dados.csv', index=False)