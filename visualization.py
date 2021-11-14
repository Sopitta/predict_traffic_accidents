import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

path ='traffic_accidents.csv'
data = pd.read_csv(path)
columns = data.columns

#keep just the first five columns
data.drop(columns[5:len(columns)+1], axis=1,inplace=True)
#print(data['MONAT'].unique())
#remove the rows 
data['MONAT'] = data['MONAT'].apply(lambda x: x[-2:])
data = data.loc[data['MONAT'] != 'me']
print(data['JAHR'].unique())
data_alko = data.loc[data['MONATSZAHL'] == 'Alkoholunfälle']
data_alko_2020 = data_alko.loc[data_alko['JAHR'] == 2001]
sns.set(font_scale=1.5, style="whitegrid")
sns.lineplot(data=data.loc[data['JAHR'] == 2001], x="MONAT", y="WERT",hue ="AUSPRAEGUNG",style="MONATSZAHL")
plt.show()

#print(data.groupby(['MONATSZAHL']).size())
#print(data.groupby(['AUSPRAEGUNG']).size())