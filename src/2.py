import pandas as pd
df = pd.read_csv('your_data.csv')
df['new_column'] = df['column1'] * 2 + df['column2']
print(df)