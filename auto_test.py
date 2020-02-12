import pandas, os, pickle
from scipy.sparse import find

#Task 1
#read the file "ecoinvent_activity_overview.xlsx".  
#The tab "activity overview" contains all the outputs to technosphere of each dataset of ecoinvent.  
#The activity overview contains the following information:
#activity name, geography, special activity type, group, exchange name, amount
#We want to keep only the exchanges in the group reference products, and datasets of special activity type "market activity"
#We also want to write the unit of the exchange, as found in the units tab.  
#Finally, we want to write the result back to excel.
filename = 'ecoinvent_activity_overview.xlsx'
dfs = pandas.read_excel(filename, None, keep_default_na = False, na_values = [''])
df = dfs['activity overview'].copy()
df = df[df['special activity type'] == 'market activity']
df = df[df['group'] == 'reference product']
index = 'exchange name'
df = df.set_index(index)
units = dfs['units'].set_index(index)
df = df.join(units).reset_index()
result_filename = 'markets_only.xlsx'
df.to_excel(result_filename, index = False)

#useful resources
#https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.join.html
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_excel.html

#Task 2
#the file "matrix.pkl" contains is a large sparse matrix.  
#Rows of the matrix represent pollution streams to environment
#columns represent datasets
#The coefficient 3.2 in position (2, 4) means that each time 1 unit of the dataset 4 is produced, 
#3.2 units of the pollutant in position 2 is emitted.
#The name and unit of datasets and pollutants are saved in files "datasets.pkl" and "pollutants.pkl".
#Wrtie a script that prints the name of the dataset and the list of the pollutants, with their quantities, 
#for each of the datasets
