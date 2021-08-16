import pandas as pd

#read excel files to dataframes
df = pd.read_excel(r'COGS_dataframe.xlsx')
df1 = pd.read_excel(r'Class_dict.xlsx')

df2 = pd.read_excel(r'income_df.xlsx')

#concat cogs and income so that class and job name are same column 
df5 = pd.concat([df,df2],sort=False)

# print(df5.head)

# merge the two dataframes
results = pd.merge(df5,df1,on='Class')



# like a pivot table, groups the area and job names and adds a count coloumn
results = results.groupby(['Area','Name']).size().reset_index(name='counts')

results.to_excel('raw_data_merge.xlsx')

nam= results['Name']
results = results[nam.isin(nam[nam.duplicated()])].sort_index()

# print(results)
results = results.reset_index()


results.to_excel('Output.xlsx')
# Look for duplicates  if multiple jobs appear in this table, it is ether a job that 
# maintanance and consturction share, or its a error in coding

# df4 = df3.duplicated(subset='Name',keep = False)

# # join the grouped df with theboolean column 
# df5= pd.concat([df3,df4],axis=1,join_axes=[df3.index])

# # had to reaname the column headers so i could filter 
# df5.columns = ['a','b','c','d']

# df6 =df5[df5['d']== True]
# print(df6)