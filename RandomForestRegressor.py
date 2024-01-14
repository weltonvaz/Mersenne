import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn import metrics
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict
from sklearn.ensemble import RandomForestRegressor

# Carregue seus dados
data = pd.read_csv('divisores2.csv', encoding='utf-8', sep=',')
# Pré-processamento e divisão dos dados
X = data.drop('Divisores', axis=1)
y = data['Divisores']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Treinamento do modelo
model = RandomForestRegressor(n_estimators=100, random_state=0)
model.fit(X_train, y_train)

# Fazer previsões
# predictions = model.predict(X_test)

# Fazer previsões
test_value = np.array([1000081]).reshape(-1, 1)  # Substitua por seus próprios dados de teste
predictions = model.predict(test_value)

print(predictions)