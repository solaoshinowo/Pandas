# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 15:21:28 2019

@author: sola
"""

"""
Spyder Editor

This is a temporary script file.
"""
"to read or load data from an external file into jupter"
import numpy as np
import pandas as pd
pd.read_csv('abc.csv', delimiter = ',')


"to add column names when reading or loading data from an external file into jupter"

pd.read_csv('abc.csv', delimiter=';', names = ['my_datetime', 'event', 'country', 'user_id', 'source', 'topic'])


"to store values to the screen,so you can print it later"
document_read = pd.read_csv('pandas_tutorial_read.csv', delimiter=';', names = ['my_datetime', 'event', 'country', 'user_id', 'source', 'topic'])


"to print the stored value"
document_read


"to pick specific columns of your dataframe"
document_read[['country', 'user_id']]

"to change the order the specific columns of your dataframe are displayed"
document_read[['user_id', 'country']]