import pandas as pd
import os

files = [file for file in os.listdir('./SalesAnalysis/Sales_Data')]

all_months = pd.DataFrame()
for file in files:
    all_months = pd.concat([all_months, pd.read_csv(f'./SalesAnalysis/Sales_Data/{file}')])

#all_months.to_csv('./SalesAnalysis/all_month_data', index=False)
