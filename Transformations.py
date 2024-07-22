import pandas as pd
data = pd.read_csv('machine-readable-business-employment-data-mar-2024-quarter(in).csv')

one_data = data.drop(columns=['Suppressed','Series_title_4', 'Series_title_5'])
one_data['Period'] = one_data['Period'].astype(str)
one_data['year'] = one_data['Period'].str.split('.').str[0]
two_data = one_data.groupby(['year', 'Series_reference']).Data_value.sum()
two_data = two_data.groupby('Series_reference').max()
print(two_data)
#third_data = one_data.Data_value.isnull().groupby('Series_reference')
#print(third_data)
