import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime


st.title ("Dashboard 1")

raw_csv_data= pd.read_csv("md3.csv")
df_comp=raw_csv_data[:800]

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

del data['Date']
del data['Weekly_Sales']

data.columns = ["Date","Department 1", "Department 2", "Department 3", "Department 4"]



data1 = data.copy()

#Sidebar Code
st.sidebar.subheader("Navigation Bar")
rad = st.sidebar.radio("Select One of the following Options", {'Line Chart', 'Yearwise Avg Sales Data', 'Queries Table' })

if rad == 'Line Chart':
    #Linechart Selectbox
    yval= st.selectbox("Enter the Department",["Department 1", "Department 2", "Department 3", "Department 4", "Department 5","All"],index=0)

    if yval == 'All':
        yval = None

    #Linechart plot
    st.line_chart(data1, x='Date', y=yval)


    #Plotly Plot
    if yval == None:
        x1= list(data1['Date'])
        fig, ax = plt.subplots()
        ax.plot(x1,list(data1['Department 1']), label="P1")
        ax.plot(x1,list(data1['Department 2']))
        ax.plot(x1,list(data1['Department 3']))
        ax.plot(x1,list(data1['Department 4']))
        ax.plot(x1,list(data1['Department 5']))


        plt.xlabel("Date")
        plt.ylabel("Sales of Department")

        st.pyplot(fig)

    else:
        x1= list(data1['Date'])
        y1= list(data1[yval])
        fig, ax = plt.subplots()
        ax.plot(x1,y1)

        plt.xlabel("Date")
        plt.ylabel("Sales of Department")

        st.pyplot(fig)


if rad == 'Yearwise Avg Sales Data':
    #Yearwise Avg Monthly Sales Table
    dataY = data1
    yrs= []
    for index in data1.index:
        x=data1.loc[index,'Date']
        y = x.year
        yrs.append(y)

    dataY['Year_W']= yrs

    avg = st.selectbox("Enter the Department", ["Department 1", "Department 2", "Department 3", "Department 4", "Department 5"], index=0)
    key_sales_column = avg

    avg_sales = dataY.groupby('Year_W')[key_sales_column].mean().round()
    avg_sales = avg_sales.reset_index()

    Year = avg_sales['Year_W']
    Average_Sales = avg_sales[key_sales_column]

    fig = plt.figure(figsize=(15, 8))
    plt.bar(Year, Average_Sales, width=0.4, color='maroon')#Can change Bar Chart Parameters Width is for bar width
    plt.xlabel('Year')
    plt.ylabel(f'Average Sales Of {avg}')
    plt.title('Bar Chart Showing the Average Sales of Department in each Year')
    st.pyplot(fig)



if rad == 'Queries Table':
    #Query Table
    st.subheader ('Run your Queries here')

    #Date Range
    da1= st.date_input("Enter Start Date in YYYY/MM/DD format",value = datetime.date(2013, 11, 1),min_value = datetime.date(2011, 11, 1))
    da2= st.date_input("Enter End Datein YYYY/MM/DD format", value = datetime.date(2017, 8, 1),min_value = datetime.date(2011, 11, 1), max_value = datetime.date(2017, 8, 1))

    sam = data1[data1['Date'] >= da1 ]
    sam1 = sam[sam['Date'] <= da2 ]

    #Value Range

    st.write("Choose the Departments for which you want to set a range")

    p1v=[0,32]
    p2v=[84,9456]
    p3v=[6,2178]
    p4v=[156,566]
    p5v=[150,19605]

    cb1 = st.checkbox("Department 1",value=False)
    if cb1:
        p1v = st.slider("Department 1", value=[0,32], min_value=0, max_value=32, key='slider1keys')

    cb2 = st.checkbox("Department 2",value=False)
    if cb2:
        p2v = st.slider("Department 2", value=[84,9456], min_value=0, max_value=32, key='slider1keys2')

    cb3 = st.checkbox("Department 3",value=False)
    if cb3:
        p3v = st.slider("Department 3", value=[6,2178], min_value=0, max_value=32, key='slider3keys')

    cb4 = st.checkbox("Department 4",value=False)
    if cb4:
        p4v = st.slider("Department 4", value=[156,566], min_value=0, max_value=32, key='slider4keys')

    cb5 = st.checkbox("Department 5",value=False)
    if cb5:
        p5v = st.slider("Department 5", value=[150,19605], min_value=0, max_value=32, key='slider5keys')

    d1 = sam1[sam1['Department 1'] >= p1v[0] ]
    d11= d1[d1['Department 1'] <= p1v[1] ]

    d2 = d11[d11['Department 2'] >= p2v[0] ]
    d22= d2[d2['Department 2'] <= p2v[1] ]

    d3 = d22[d22['Department 3'] >= p3v[0] ]
    d33= d3[d3['Department 3'] <= p3v[1] ]

    d4 = d33[d33['Department 4'] >= p4v[0] ]
    d44= d4[d4['Department 4'] <= p4v[1] ]

    d5 = d44[d44['Department 5'] >= p5v[0] ]
    d55= d5[d5['Department 5'] <= p5v[1] ]

    #Tables to display
    cdisp = st.multiselect("Select the Columns to Display", ["Date","Department 1", "Department 2", "Department 3", "Department 4", "Department 5"])
    cdisp.sort()
    st.dataframe(d55[cdisp])
