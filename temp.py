# -*- coding: utf-8 -*-

 
#some basic operations
import os

os.getcwd() #get current working directory

os.listdir()#list fies in the directory

globals() #list all functions

#delete an object
x = 5*25
x
del(x)

# Creating a data frame “df” of dimension 6x4 (6 rows and 4 columns) containing random numbers

import numpy as np
import pandas as pd

df = np.random.randn(6,4)
df = pd.DataFrame(df)

#row and column names
df.index
df.columns
#see the top & bottoms
df.head(1) #1st row
df.tail(1) #second row
df.shape #dimension
len(df) # length of df

df.describe() #return the quick summary 

df.index = ["A","B","C","D","E","F"]#change the row names
df.columns = ['P','Q','R','S']#change the column names
#sorting
df.sort_values(by=['P'],inplace=True)#sort P colummn as ascending order
df.sort_values(by=['Q'],inplace=True,ascending=False)#sort Q colummn as descending order

#Slicing rows from df
df[0:3] #slice from 1st to 3rd row
#slicing from columns
df.loc[:,['R','S']] #have to specify the col names
df.iloc[0:3,0:3] #both row and column slicing
df.iat[3,3] #specified value of row/column

#          Data Frame: Data selection

df[df.R>0]



