import pandas as pd
data = pd.read_csv('sculptures.csv')

data['Museon scultures'] = data['LocationPlace'].str.contains(r'Музеон|МУЗЕОН', regex=True)
data['Not bronze'] = ~data['Material'].isin(['Бронза'])
result = data.groupby(['Museon scultures','Not bronze'])['ManufactYear'].mean()
print(result[True,True])
