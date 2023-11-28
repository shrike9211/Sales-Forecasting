import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

raw_csv_data= pd.read_csv("md3.csv")

df_comp = raw_csv_data.copy()
df_comp.date = pd.to_datetime(df_comp.Date, dayfirst = True)
del df_comp['Store']
del df_comp['IsHoliday']
del df_comp['Dept']

data1 = df_comp[:143]
data2 = df_comp[143:286]
data3 = df_comp[286:429]
data4 = df_comp[429:572]
data5 = df_comp[572:715]

d2 = []
d2[0:143] = data2.Weekly_Sales

d3 = []
d3[0:143] = data3.Weekly_Sales

d4 = []
d4[0:143] = data4.Weekly_Sales

d5 = []
d5[0:143] = data5.Weekly_Sales

data = data1.copy()
data['dept1'] = data1.Weekly_Sales
data['dept2'] = d2
data['dept3'] = d3
data['dept4'] = d4
data['dept5'] = d5

##

data.columns = ["Date","Department 1", "Department 2", "Department 3", "Department 4", "Department 5"]


del data['Date']
del data['Weekly_Sales']

data1 = data.copy()

print(data1)