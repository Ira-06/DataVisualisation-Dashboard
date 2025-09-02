import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# This is a commade you use to write onto the sytem and it using some functionality of steamlit will write it onto the webpage
# you can run anything here
# st.write ("Hello World")

#for i in range (10):
#   st.write ("This is line number ", i)
#

st.title("Data Dashboard")

#To upload a file, we use the widget provided by streamlit
uploaded_file= st.file_uploader("Select a CSV File", type = "csv")

if uploaded_file is not None :
    st.write ("File Successfully Uploaded")
    
    df = pd.read_csv(uploaded_file)
    
    st.subheader("Data Preview")
    # To show the data in a tabular format
    # df.head function will show the first 5 rows of the dataframe
    st.write(df.head())
    
    st.subheader("Data Summary")
    st.write(df.describe())
    
    st.subheader("Filtered Data")
    columns= df.columns.tolist()
    # SELECT the column to filter on 
    selected_columns= st.selectbox("Select Column to Filter", columns)
    
    # Find the unique values in the selected column
    unique_values = df[selected_columns].unique()
    
    # SELECT From the unique values found, select the vaules whose data you would like to see
    selected_unique_value= st.selectbox ("Select the Value to filter based on ", unique_values)
    
    # Filtered_data get only those row, from the selected values whose unique values match the selected_unique_value
    filtered_data = df[df[selected_columns] == selected_unique_value]
    
    # Display that filtered data
    st.write(filtered_data)
    
    # Plotting THIS unique selection 
    
    st.subheader("Data Visualization")
    x_plot_columns= st.selectbox("Select X-axis Columns to Plot", columns)
    y_plot_columns= st.selectbox("Select Y-axis Columns to Plot", columns)
    
    if st.button("Generate Plot"):
        st.line_chart(filtered_data.set_index(x_plot_columns)[y_plot_columns])
        
else :
    st.error("Please upload a CSV file to proceed")
        
