import pandas as pd
import random

data = []
for i in range(100):
    amount = round(random.uniform(1, 1000), 2)
    location = random.choice(['US', 'UK', 'IN'])
    fraud = random.choice([0, 1])
    data.append([i, amount, location, fraud])

df = pd.DataFrame(data, columns=['TransactionID', 'Amount', 'Location', 'Fraud'])
df.to_csv('transactions.csv', index=False)
print("Dataset created!")
