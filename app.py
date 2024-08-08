import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd

def create_frontend():
    # Load data from CSV files
    Detail_5308 = pd.read_csv('Detail_5308.csv')
    Temp_5308 = pd.read_csv('Temp_5308.csv')
    Detail_5329 = pd.read_csv('Detail_5329.csv')
    Temp_5329 = pd.read_csv('Temp_5329.csv')

    # Data for pie charts
    soh_cell_5308 = 99.734
    soh_cell_5329 = 94.08533333333334
    unhealthy_5308 = 100 - soh_cell_5308
    unhealthy_5329 = 100 - soh_cell_5329

    labels = ['Healthy', 'Unhealthy']
    values_5308 = [soh_cell_5308, unhealthy_5308]
    values_5329 = [soh_cell_5329, unhealthy_5329]

    fig_pie = go.Figure()
    fig_pie.add_trace(go.Pie(labels=labels, values=values_5308, name="SOH_CellID_5308", hole=.3, domain={'x': [0, 0.5]}))
    fig_pie.add_trace(go.Pie(labels=labels, values=values_5329, name="SOH_CellID_5329", hole=.3, domain={'x': [0.5, 1]}))
    fig_pie.update_layout(title_text='Battery State of Health for Cells 5308 and 5329',
                          annotations=[dict(text='Cell 5308', x=0.18, y=0.5, font_size=20, showarrow=False),
                                       dict(text='Cell 5329', x=0.82, y=0.5, font_size=20, showarrow=False)])

    # Plots for CELL ID 5308
    fig_voltage_5308 = px.line(Detail_5308, x='Absolute Time', y='Voltage(V)', title='Voltage vs Time')
    fig_current_5308 = px.line(Detail_5308, x='Absolute Time', y='Cur(mA)', title='Current vs Time')
    fig_temperature_5308 = px.line(Temp_5308, x='Realtime', y='Auxiliary channel TU1 T(°C)', title='Temperature vs Time')
    fig_capacity_5308 = px.line(Detail_5308, x='Absolute Time', y='CapaCity(mAh)', title='Capacity vs Time')

    fig_line_5308 = make_subplots(
        rows=2, cols=2,
        subplot_titles=('Voltage vs Time', 'Current vs Time', 'Temperature vs Time', 'Capacity vs Time')
    )

    fig_line_5308.add_trace(fig_voltage_5308['data'][0], row=1, col=1)
    fig_line_5308.add_trace(fig_current_5308['data'][0], row=1, col=2)
    fig_line_5308.add_trace(fig_temperature_5308['data'][0], row=2, col=1)
    fig_line_5308.add_trace(fig_capacity_5308['data'][0], row=2, col=2)

    fig_line_5308.update_layout(
        title_text='Subplots of Various Metrics CELL ID 5308',
        height=800,
        width=1000,
        autosize=False
    )

    # Plots for CELL ID 5329
    fig_voltage_5329 = px.line(Detail_5329, x='Absolute Time', y='Voltage(V)', title='Voltage vs Time')
    fig_current_5329 = px.line(Detail_5329, x='Absolute Time', y='Cur(mA)', title='Current vs Time')
    fig_temperature_5329 = px.line(Temp_5329, x='Realtime', y='Auxiliary channel TU1 T(°C)', title='Temperature vs Time')
    fig_capacity_5329 = px.line(Detail_5329, x='Absolute Time', y='CapaCity(mAh)', title='Capacity vs Time')

    fig_line_5329 = make_subplots(
        rows=2, cols=2,
        subplot_titles=('Voltage vs Time', 'Current vs Time', 'Temperature vs Time', 'Capacity vs Time')
    )

    fig_line_5329.add_trace(fig_voltage_5329['data'][0], row=1, col=1)
    fig_line_5329.add_trace(fig_current_5329['data'][0], row=1, col=2)
    fig_line_5329.add_trace(fig_temperature_5329['data'][0], row=2, col=1)
    fig_line_5329.add_trace(fig_capacity_5329['data'][0], row=2, col=2)

    fig_line_5329.update_layout(
        title_text='Subplots of Various Metrics CELL ID 5329',
        height=800,
        width=1000,
        autosize=False
    )

    st.title("Battery Metrics Dashboard")
    tab1,tab2,tab3=st.tabs(["Pie","Line","Grid"])
    with tab1:
        st.plotly_chart(fig_pie)
    with tab2:
        st.plotly_chart(fig_line_5308)
    with tab3:
        st.plotly_chart(fig_line_5329)

if __name__ == "__main__":
    create_frontend()
