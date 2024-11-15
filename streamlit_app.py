import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

# datasets
df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'Prediction Model': [10, 15, 12, 18, 20],
    'Actual': [5, 8, 11, 14, 17]
})

labels = ['Category A', 'Category B', 'Category C', 'Category D']

st.set_page_config(layout="wide")
st.sidebar.header('Sidebar')

st.title("🛬 Viggo Prediction Model 🛫")
st.write(
    "Prediction model here, zeg maar waar die foto nu is."
)

st.image('schiphol.jpg')

# Sidebar
st.sidebar.write('Pie charts met de verdeling van de oorzaken voor vertragingen op basis van de processen, of de verdeling van vluchten die optijd of te laat zijn. en Features om het model te tunen')
selected_lines = st.sidebar.multiselect('Choose lines to display', df.columns[1:])


# Tabs
plane, ground, travelers = st.tabs(["Airplane", "Ground Crew", "Passengers"])

with plane:
    st.header('Delays related to movements of the airplane')

    # Create the line plot with the selected lines
    fig = px.line(df, x='x', y=selected_lines, title='Multiple Lines Plot')

    # Display the plot in Streamlit
    st.plotly_chart(fig)

with ground:

    st.header('Delays related to the ground crew tasks')

    # Sample data
    labels = ['Category A', 'Category B', 'Category C', 'Category D']
    values = [15, 30, 45, 10]

    # Create the histogram using Plotly
    fig2 = px.histogram(x=labels, y=values, title='Histogram')

    # Display the chart in Streamlit
    st.plotly_chart(fig2)

with travelers:
    st.header('Delays related to passengers and boarding')
    
    # Sample data
    labels = ['Category A', 'Category B', 'Category C', 'Category D']
    values = [15, 30, 45, 10]

    # Create the pie chart using Plotly
    fig3 = px.pie(values=values, names=labels, title='Interactive Pie Chart')

    # Customize the chart (optional)
    fig3.update_traces(textposition='inside', textinfo='percent+label')

    # Display the chart in Streamlit
    st.plotly_chart(fig3)
