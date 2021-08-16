import pandas as pd

#read excel files to dataframes
df = pd.read_excel(r'COGS_dataframe.xlsx')
df1 = pd.read_excel(r'Class_dict.xlsx')

df2 = pd.read_excel(r'income_df.xlsx')

#concat cogs and income so that class and job name are same column 
df5 = pd.concat([df,df2],sort=False)


# merge the two dataframes
results = pd.merge(df5,df1,on='Class')



# group the area and job names and adds a count coloumn
results = results.groupby(['Area','Name']).size().reset_index(name='counts')

results.to_excel('raw_data_merge.xlsx')

nam= results['Name']

# filter the df results with only those job names that are duplicates 
results = results[nam.isin(nam[nam.duplicated()])].sort_index()

# print(results)
results = results.reset_index()


results.to_excel('Output.xlsx')
