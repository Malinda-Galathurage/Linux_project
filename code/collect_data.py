import pandas as pd

file_path = '../data/malinda_data.csv'
data = pd.read_csv(file_path)

data_info = data.info()
data_head = data.head()

data_info, data_head

data['Age'].fillna(data['Age'].median(), inplace=True)

data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)

data['HasCabin'] = data['Cabin'].notnull().astype(int)
data.drop(columns=['Cabin'], inplace=True)


data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})

data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)

data.drop(columns=['Name', 'Ticket'], inplace=True)

data.to_csv('../data/preprocessed_data.csv', index=False)
print("Data collection completed by Vithya")
