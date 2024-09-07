import joblib
import pandas as pd


model = joblib.load('../models/vithya_model.pkl')

new_data = pd.read_csv('../data/preprocessed_data.csv')

X_new = new_data.drop(['PassengerId' , 'Survived'], axis=1)

predictions = model.predict(X_new)

new_data['Predictions'] = predictions
print(new_data[['PassengerId', 'Predictions']])


new_data.to_csv('../data/vithya_predictions.csv', index=False)
print("Predictions saved to vithya_predictions.csv")
