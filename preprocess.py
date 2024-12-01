import pandas as pd

df = pd.read_csv('data.csv')
df['age'] = df['age'] * 2  # Double the ages for demo
df.to_csv('processed_data.csv', index=False)