# %%
import os
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import datetime
import seaborn as sns

#%%
# Read in wl_data2
filepath = os.path.join('/Users/matthewford/Desktop/Python files/Output_files/wl_data2.csv')
print(filepath)

wl_data2 = pd.read_csv(filepath)
pd.options.display.float_format = '{:.2f}'.format
print(wl_data2.info())

#%% 
# Create a pivot table basin and avg depth
pivot1 = pd.pivot_table(wl_data2, index='basinid', values='depth', aggfunc=['mean'])
print(pivot1)

#%% 
# Save pivot table 1 to a csv in the specified directory 
pivot1.to_csv('/Users/matthewford/Desktop/Python files/Output_files/avgwldepth_bybasin.csv')

#%%
# Create a pivot table wellid and avg depth
pivot2 = pd.pivot_table(wl_data2, index='wellid', values='depth', aggfunc=['mean'])
print(pivot2)

#%% 
# Save pivot table 2 to a csv in the specified directory 
pivot2.to_csv('/Users/matthewford/Desktop/Python files/Output_files/avgwldepth_bywellid.csv')

#%%
# dont think this set is necessary but it is good to know and may need in future
#set index of dataframe by date [] makes it a multiindex if u want
wl_data2.set_index('date')

#%%
# extract the year from the date column and create a new column year
wl_data2['year'] = pd.DatetimeIndex(wl_data2['date']).year

#%%
# Create a pivot table of avg water depth by basin and by year
pivot3 = pd.pivot_table(wl_data2, index=['basinid','year'], values='depth', aggfunc=['mean'])
print(pivot3)

#%%
wl_data_basin = pivot3.unstack(level=1)
print(wl_data_basin)

#%% 
# Save pivot table 3 to a csv in the specified directory 
pivot3.to_csv('/Users/matthewford/Desktop/Python files/Output_files/avgwldepth_bybasin&year.csv')

#%%
# Create a pivot table of avg water depth by well id and year
pivot4 = pd.pivot_table(wl_data2, index=['wellid','year'], values='depth', aggfunc=['mean'])
print(pivot4)

#%% 
# Save pivot table 4 to a csv in the specified directory 
pivot4.to_csv('/Users/matthewford/Desktop/Python files/Output_files/avgwldepth_bywellid&year.csv')

#%%
# create a dataframe wl_data3 which unstacks pivot table 4 so rows are wellid and columns are each year
wl_data3 = pivot4.unstack(level=1)
print(wl_data3)

#%%
#Create a variable called "myid" to make locating graphing wells easier
myid=395909110530701

# %%
# take pivot4 and locate all the water levels by year for the given wellid
pivot4.loc[myid]

#%%
# plot the wellid identified by "myid" by wl depth and year 
fig, ax = plt.subplots()
ax.plot(pivot4.loc[myid],label=myid)
ax.set(title='Depth To Water', xlabel='Year', ylabel='Depth(ft)')
ax.legend()
ax.grid()
plt.show

#Save plot as a png with the myid name to the specified directory
type = myid
plt.savefig('/Users/matthewford/Desktop/Python files/Output_files/{0}.png'.format(type), bbox_inches='tight')

#%%
#list of wells that we want to plot
wl_data2.dropna(subset=['depth'],inplace=True)
basin='AGF'
mylist=wl_data2[wl_data2['basinid']==basin]['wellid'].unique()
# looking at what was causing our issues is the 2 lines below
#seti=216
#wl_data2[wl_data2['wellid']==mylist[seti]]

# plot the wellid identified by "myid" by wl depth and year 
fig, ax = plt.subplots()
ax.plot(pivot4.loc[mylist[0]],label=mylist[0])
ax.set(title='Depth To Water', xlabel='Year', ylabel='Depth(ft)')


for i in range(1,len(mylist)):
    print(i)
    ax.plot(pivot4.loc[mylist[i]],label=mylist[i])
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
ax.grid()
plt.show

#%%
#unstack pivot3 into a df called wl_data_basin to be able to plot
wl_data_basin = pivot3.unstack(level=0)
print(wl_data_basin)

#%%
# plot the wellid identified by "myid" by wl depth and year 
fig, ax = plt.subplots()
ax.plot(wl_data_basin)
ax.set(title='Depth To Water', xlabel='Year', ylabel='Depth(ft)')
#can plot different x scales
plt.xlim(2018,2019)
#can plot different y scales
plt.ylim(0,500)
ax.legend()
ax.grid()
plt.show

#%%
# Cant get a boxplot i dont understand in seaborn or matplotlib
sns.boxplot(x='year', y='basinid', data=wl_data_basin2)
# %%
