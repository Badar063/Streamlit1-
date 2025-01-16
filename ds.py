import numpy as np
import pandas as numpy
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as pyplot
from scipy.stats import gaussian_kde
st.title('My First Data Science Project')
st.subheader('Lets Start')
data_opt=['iris','tips', 'titanic']
data_select=st.selectbox('Select Dataset', data_opt)
if data_select=='iris':
    df=sns.load_dataset('iris')
if data_select=='tips':
    df=sns.load_dataset('tips')
if data_select=='titanic':
    df=sns.load_dataset('titanic')
else:
    st.write('No Data Found')
upload_file=st.file_uploader('Select Fie', type=['csv', 'xlsx']) 
if upload_file is not None:
    df=pd.read_csv(upload_file) 
st.write(df.info()) 
st.write('Number of Rows', df.shape[0])
st.write('Number of Columns', df.shape[1])
st.write(f'Name of COlumns and Their Data types', df.dtypes)
st.write(df.shape)
st.write(df.head()) 
st.write('Summary', df.describe())    
#Printing Null Values
if df.isnull().sum().sum()>0:
    st.write('Null Values', df.isnull().sum().sort_values(ascending=False))
else:
    st.write('No Null Values')    
#Visualizations
x_axis=st.selectbox('X-Axis', df.columns)
y_axis=st.selectbox('Y-Axis', df.columns)
plt_type=st.selectbox('Select Plot', ['Line','Scatter','Bar', 'Hist', 'Box' ,'KDE'])
if plt_type=='Line':
    st.line_chart(df[[x_axis, y_axis]])
elif plt_type=='Scatter':
    st.scatter_chart(df[[x_axis, y_axis]])
elif plt_type=='Box':
    st.bar_chart(df[[x_axis, y_axis]])  
elif plt_type=='Hist':
    df[x_axis].plot(kind='hist')
    st.pyplot()
elif plt_type=='Box':
    df[[x_axis, y_axis]].plot(kind='box') 
    st.pyplot()
elif plt_type=='KDE':
    df[[x_axis, y_axis]].plot(kind='kde') 
    st.pyplot()
#Selections
st.subheader('Pair Plots')
st.pyplot(sns.pairplot(df))
st.pyplot(sns.pairplot(df, hue='species', markers='o'))
sel_col=st.selectbox('Select Column of your choice', df.columns)
st.pyplot(sns.pairplot(df, hue=sel_col)) #Don;t write in quote
#Heatmap    
st.subheader('Heatmap')
numeric_col=df.select_dtypes(include=np.number).columns
corr_matrix=df[numeric_col].corr()
#st.plotly_chart(sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=2)) It creates problem in sns
import plotly.graph_objects as go
fig=go.Figure(data=go.Heatmap(z=corr_matrix.values,
x=corr_matrix.columns,
y=corr_matrix.columns,
colorscale='Viridis'
))
st.plotly_chart(fig)
