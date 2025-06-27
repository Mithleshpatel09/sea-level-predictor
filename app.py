import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

# Import the draw_plot function from your sea_level_predictor.py file
# Ensure sea_level_predictor.py is in the same directory as app.py
# If your sea_level_predictor.py already calls draw_plot() at the end
# with 'if __name__ == "__main__":', you might want to remove that to avoid double plotting

# We are going to put the logic directly here to ensure it works smoothly with Streamlit
# Alternatively, you could just call sea_level_predictor.draw_plot() if it returns the figure object correctly

st.set_page_config(layout="wide", page_title="Sea Level Predictor") # App ka layout aur title set kiya

st.title("🌊 Global Sea Level Predictor")
st.write("This app visualizes historical sea level data and predicts future trends using linear regression.")

# --- Data Loading and Plotting Logic (from sea_level_predictor.py's draw_plot function) ---

# Read data from file
try:
    df = pd.read_csv('epa-sea-level.csv') # Make sure this CSV is in the same folder
except FileNotFoundError:
    st.error("Error: 'epa-sea-level.csv' not found. Please ensure it's in the same directory.")
    st.stop() # Stop the app if data is not found

# Create scatter plot
fig, ax = plt.subplots(figsize=(10, 6)) # Create a figure and axes object
ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

# Create first line of best fit (using all data 1880-2013)
res1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
years_predict1 = pd.Series(range(1880, 2051))
ax.plot(years_predict1, res1.intercept + res1.slope * years_predict1, 'r', label='Fit 1880-2013')

# Create second line of best fit (using data from year 2000 onwards)
df_recent = df[df['Year'] >= 2000]
res2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
years_predict2 = pd.Series(range(2000, 2051))
ax.plot(years_predict2, res2.intercept + res2.slope * years_predict2, 'g', label='Fit 2000-2013')

# Add labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Sea Level (inches)')
ax.set_title('Rise in Sea Level')
ax.grid(True)
ax.legend()

# Set x-axis ticks to match test expectations (FreeCodeCamp specific)
xticks = np.arange(1850, 2076, 25)
ax.set_xticks(xticks)
ax.set_xticklabels(xticks.astype(int))

# Display the plot in Streamlit
st.pyplot(fig)

st.subheader("Data Overview")
st.dataframe(df.head()) # Dataframe ke pehle 5 rows dikhao

st.write("""
**Model Summary:**
* **Overall Trend (1880-2013):** The sea level has been steadily rising.
* **Recent Acceleration (2000 onwards):** The rate of sea level rise appears to have accelerated significantly in the 21st century.
""")