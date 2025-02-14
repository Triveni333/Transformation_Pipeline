import pandas as pd
data = pd.read_csv('machine-readable-business-employment-data-mar-2024-quarter(in).csv')

one_data = data.drop(columns=['Suppressed','Series_title_4', 'Series_title_5'])
print(one_data)

one_data['Period'] = one_data['Period'].astype(str)
one_data['year'] = one_data['Period'].str.split('.').str[0]
two_data = one_data.groupby(['year','Series_reference']).Data_value.sum().reset_index()

mapping_dict = {} 
for i, row in two_data.iterrows():
    if row['Series_reference'] in mapping_dict.keys() : 
        if row['Data_value'] > mapping_dict[row['Series_reference']]['Data_value'] :
            mapping_dict[row['Series_reference']]['year'] = row['year']
            mapping_dict[row['Series_reference']]['Data_value'] = row['Data_value']
    else :
        mapping_dict[row['Series_reference']] = {}
        mapping_dict[row['Series_reference']]['year'] = row['year']
        mapping_dict[row['Series_reference']]['Data_value'] = row['Data_value']


transform = pd.DataFrame.from_dict(mapping_dict, orient='index', columns=['year', 'Data_value'])
print(transform)
    
third_data = data[data.Data_value.notnull()]
third_data.to_csv('No missing data values.csv')
print(third_data)

data['Data_value'] = data.groupby('Series_reference')['Data_value'].transform(sum)
data.to_csv('Total value of each series.csv')
print(data)
