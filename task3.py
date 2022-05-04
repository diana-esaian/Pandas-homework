import pandas as pd
data = pd.read_csv('sculptures.csv')

result = data[data['Longitude_WGS84']>55.0]['global_id']
print(int(result))
