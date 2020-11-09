
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
# create a dataframe Pump_data3 which unstacks pivot table 1 so wellid=row &
Pump_data_all = pivot1.unstack(level=1)
print(Pump_data_all)

#%%
#Create a variable called "myid" to make locating graphing wells easier
myid=345434110171201

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
#pump_data1 = pivot2.unstack(level=1)
#print(pump_data1)

#%%
# create and locate a variable for the basin we want 
mybasinid='PINAL AMA'
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
#Unstack pivot 2 into nnew df called pump_data1 
pump_data1 = pivot2.unstack(level=0)
print(pump_data1)

#%%
#Plot all of the basins by year and Af pumped
fig, ax = plt.subplots()
ax.plot(pump_data1)
ax.set(title='Acre Feet Pumped', xlabel='year', ylabel='Volume Pumped (AF)')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
ax.grid()
plt.show

#Save plot as png to the specified directory
plt.savefig('/Users/matthewford/Desktop/Python files/Output_files/AFPumped_ByBasin.png', bbox_inches='tight')
# %%
