import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('transactions.csv')
le = LabelEncoder()
df['Location'] = le.fit_transform(df['Location'])

X = df[['Amount', 'Location']]
y = df['Fraud']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
df.loc[X_test.index, 'Predicted_Fraud'] = predictions
df.to_csv('transactions_with_predictions.csv', index=False)
print("ML predictions done and saved!")
