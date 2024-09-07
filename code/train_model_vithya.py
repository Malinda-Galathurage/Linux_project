from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pandas as pd


df = pd.read_csv('../data/preprocessed_data.csv')


X = df.drop(['PassengerId', 'Survived'], axis=1)
y = df['Survived']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = DecisionTreeClassifier()
model.fit(X_train, y_train)

print("Model training completed by Vithya.")
