import random

import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

# Setup
st.set_page_config(page_title="BuzzGuard Mosquito Pressure Forecast", layout="wide")
st.title("🦟 BuzzGuard 14-Day Mosquito Pressure Forecast")
st.markdown("Compare mosquito activity levels across Ontario service regions.")

# Regions and forecast dates
regions = [
    "Ottawa / North Grenville",
    "Durham Region",
    "Peterborough & Kawarthas"
]
dates = [datetime.today() + timedelta(days=i) for i in range(14)]

# Generate mock forecast
def generate_forecast():
    return pd.DataFrame([
        {
            "Region": region,
            "Date": date.strftime("%Y-%m-%d"),
            "Mosquito Pressure": random.randint(2, 5)

        }
        for region in regions
        for date in dates
    ])

df = generate_forecast()

# Sidebar filter
region = st.sidebar.selectbox("Select Region", regions)
filtered = df[df["Region"] == region]

# Chart
fig = px.line(filtered, x="Date", y="Mosquito Pressure", title=f"Mosquito Pressure: {region}",
              markers=True, line_shape="spline", color_discrete_sequence=["#84cc16"])
fig.update_layout(yaxis=dict(range=[1, 5], title="Pressure Level"),
                  xaxis_title="Date")

st.plotly_chart(fig, use_container_width=True)

# Legend
st.markdown("### Pressure Levels:")
st.markdown("- 1: Low")
st.markdown("- 2: Moderate")
st.markdown("- 3: High")
st.markdown("- 4: Very High")
st.markdown("- 5: Extreme")
