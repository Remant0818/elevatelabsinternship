import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('Titanic-Dataset.csv')  
print(df.head())
print(df.info())
print(df.isnull().sum())

df['Age'].fillna(df['Age'].median(), inplace=True)

df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

df.drop(columns=['Cabin'], inplace=True)

df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])

sns.boxplot(x=df['Fare'])
plt.show()

fare_threshold = df['Fare'].quantile(0.99)
df = df[df['Fare'] < fare_threshold]

df.to_csv('cleaned_titanic.csv', index=False)

git init
git add .
git commit -m "Initial commit - Titanic preprocessing"
git remote add origin https://github.com/Remant0818/elivatelabsinternship.git
git branch -M main
git push -u origin main
