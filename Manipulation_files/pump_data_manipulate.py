
# %%
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
from glob import glob

# %%
# Read in pump_data_Full file
filepath = os.path.join('/Users/matthewford/Desktop/Python files/Output_files/Pump_Data_Full.csv')
print(filepath)

#%%
#make a datatable called cadastral_data with the read in excel file
pump_data_all = pd.read_csv(filepath)

#make scientific notation go away (needed for wellid column)
pd.options.display.float_format = '{:.2f}'.format
print(pump_data_all)

#%%
# Create a pivot table of AF Pumped by well id and year
pivot1 = pd.pivot_table(pump_data_all, index=['wellid','YEAR'], values='AF Pumped')
print(pivot1)

#%% 
# Save pivot table 1 to a csv in the specified directory 
pivot1.to_csv('/Users/matthewford/Desktop/Python files/Output_files/AFPumped_Bywellid&Year.csv')

#%%
# create a dataframe  which unstacks pivot table 1 so wellid=row &
pump_data1 = pivot1.unstack(level=1)
print(pump_data1)

#%%
# Find the number of non NAN values 
pump_data1.isnull().sum(axis=1)

#%%
#Create a variable called "myid" to make locating graphing wells easier
myid=313727111024501

# %%
# take pivot1 and locate all the AF Pumped by year for the given wellid
pivot1.loc[myid]

#%%
# plot the listed well id by wl depth and year and maniplulate the graph
fig, ax = plt.subplots()
ax.plot(pivot1.loc[myid],label=myid)
ax.set(title='Acre Feet Pumped', xlabel='Year', ylabel='Volume Pumped (AF)')
plt.ylim()
plt.xlim(1984,2020)
ax.grid()
ax.legend()
plt.show


#Save plot as a png with the myid name to the specified directory
type = myid
plt.savefig('/Users/matthewford/Desktop/Python files/Output_files/{0}.png'.format(type), bbox_inches='tight')

#%%
# Create a pivot table summing up the AF Pumped by year by basin
pivot2 = pd.pivot_table(pump_data_all, index=['Basin','YEAR'], values='AF Pumped',aggfunc=np.sum)
print(pivot2)

#%%
#Unstack pivot 2 into a new dataframe pump_data1 with basin and year
pump_data1 = pivot2.unstack(level=1)
print(pump_data1)

#%%
# create and locate a variable for the basin we want 
mybasinid='TUCSON AMA'
pivot2.loc[mybasinid]

# %%
# plot the basin id by AF Pumped & year 
fig, ax = plt.subplots()
ax.plot(pivot2.loc[mybasinid], label=mybasinid)
ax.set(title='Acre Feet Pumped', xlabel='Year', ylabel='Volume Pumped (AF)')
ax.legend()
ax.grid()
plt.show

#Save plot as a png with the myid name to the specified directory
type = mybasinid
plt.savefig('/Users/matthewford/Desktop/Python files/Output_files/{0}.png'.format(type), bbox_inches='tight')


#%%
# drop na values
pump_data1.dropna(subset=['BILL WILLIAMS'],inplace=True)

#%%
#make a list with 
mylist=pump_data1[pump_data1['AF Pumped'].unique()

#%%
#######
#######
#######
#######
#######
#######
#######
#######

fig, ax = plt.subplots()
ax.plot(pivot2.loc[mybasinid], label=mybasinid)
ax.set(title='Acre Feet Pumped', xlabel='Year', ylabel='Volume Pumped (AF)')



for i in range(1,8):
    print(i)
    ax.plot(pivot2.loc[mybasinid],label=mybasinid[i])
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
ax.grid()
plt.show


#######
#######
#######
#######
#######
#######
#######
#%%
#Unstack pivot 2 into new df called pump_data1 
pump_data1 = pivot2.unstack(level=0)
print(pump_data1)

#%%
#Create a list of basin ids so graph can make a legend
mylist=pump_data_all['Basin'].unique()
print(mylist)

#%%
#Plot all of the basins by year and Af pumped
fig, ax = plt.subplots()
ax.plot (pump_data1, label=mylist)
ax.set(title='Acre Feet Pumped', xlabel='year', ylabel='Volume Pumped (AF)')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
ax.grid()
plt.show

#Save plot as png to the specified directory
plt.savefig('/Users/matthewford/Desktop/Python files/Output_files/AFPumped_ByBasin.png', bbox_inches='tight')









#%%
pump_data_all.dropna(subset=['AF Pumped'],inplace=True)
mylist=pump_data_all['Basin'].unique()
print(mylist)

# %%
# plot the basin versus af pumped in a loop 
fig, ax = plt.subplots()
ax.plot(pivot2.loc[mylist[0]],label=mylist[0])
ax.set(title='Depth To Water', xlabel='Year', ylabel='Depth(ft)')


for i in range(1,len(mylist)):
    print(i)
    ax.plot(pump_data_all.loc[mylist[i]],label=mylist[i])
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
ax.grid()
plt.show
# %%
