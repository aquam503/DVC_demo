import pandas as pd

df = pd.read_csv('processed_data.csv')
average_age = df['age'].mean()

with open('model.txt', 'w') as f:
    f.write(f'Average age: {average_age}')