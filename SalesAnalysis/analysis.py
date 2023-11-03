import pandas as pd
import matplotlib.pyplot as plt
all_data = pd.read_csv('./SalesAnalysis/all_month_data.csv')
all_data.dropna(inplace=True)

#Data Cleaning
all_data['Month'] = all_data['Order Date'].apply(lambda x: x.split('/')[0] if isinstance(x, str) else None)
all_data['Price Each'] = pd.to_numeric(all_data['Price Each'], errors='coerce')
all_data['Quantity Ordered'] = pd.to_numeric(all_data['Quantity Ordered'], errors='coerce')
all_data = all_data[all_data['Month'] != 'Order Date']
all_data['Month'] = all_data['Month'].astype('int32')

all_data['Value'] = all_data['Quantity Ordered'] * all_data['Price Each']
all_data['City'] = all_data['Purchase Address'].apply(lambda x: x.split(',')[1] + x.split(',')[2][:3])


def get_best_month(all_data: pd.DataFrame):
    
    months = all_data.groupby('Month', as_index=False)['Value'].sum()

    return months[months.Value == max(months.Value)]['Month']

def get_best_city(all_data: pd.DataFrame):
    
    best = all_data.groupby('City', as_index=False)['Value'].sum()
    return best

best_city = get_best_city(all_data)

print(best_city)


