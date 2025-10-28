import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title='Medals Visualization', layout='wide')
st.title('Medals Visualization')

# Dropdown Menu
medal = st.selectbox('Medal Type', ['gold', 'silver', 'bronze'])

# Checkboxes
show_bar = st.checkbox('Show Bar Chart', value=True)
show_pie = st.checkbox('Show Pie Chart', value=True)

# Two-Column Structure
col1, col2 = st.columns(2)

# Load the medals wide dataset
df = px.data.medals_wide()

# Initialize chart figures
fig_bar = None
fig_pie = None

# Plot the bar chart
if show_bar:
  fig_bar = px.bar(
      df,
      x='nation',
      y=f'{medal}',
      title=f'Medals Count ({medal})'
  )

  fig_bar.update_layout(
      title_x = 0.5,
      xaxis_title = 'Country',
      yaxis_title = 'Count',
      width = 300, height = 300
  )
  
  col1.plotly_chart(fig_bar, use_container_width=True)

# Plot the pie chart
if show_pie:
  fig_pie = px.pie(
      df,
      names='nation',
      values=f'{medal}',
      title=f'Medals Count ({medal})'
  )

  fig_pie.update_layout(
      title_x = 0.5,
      width = 300, height = 300
  )
  
  col2.plotly_chart(fig_pie, use_container_width=True)
  
