import pandas as pd
data = pd.read_csv('sculptures.csv')

# Ваш код здесь

counter = data['Material'].value_counts().reset_index()
result = counter['index'].tolist()[:5]
print(result)
