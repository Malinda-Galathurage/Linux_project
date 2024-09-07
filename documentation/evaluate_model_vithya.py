from sklearn.metrics import accuracy_score
import pandas as pd
import joblib


df = pd.read_csv('../data/preprocessed_data.csv')
X_test = df.drop(['PassengerId', 'Survived'], axis=1)
y_test = df['Survived']

model = joblib.load('../models/vithya_model.pkl')


predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print(f"Model accuracy by Vithya: {accuracy}")
