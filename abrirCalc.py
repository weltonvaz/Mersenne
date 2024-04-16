import pandas as pd
import ezodf

def read_ods(filename, sheet_no=0, header=0):
    tab = ezodf.opendoc(filename=filename).sheets[sheet_no]
    return pd.DataFrame({col[header].value:[x.value for x in col[header+1:]]
                         for col in tab.columns()})

# Use a função para ler o arquivo
df = read_ods(filename='divisores2.ods')

# Agora 'df' é um DataFrame do pandas que contém os dados do seu arquivo
print(df)
