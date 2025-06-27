import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 6)) # Graph ka size set kiya
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit (1880-2013)
    res1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_predict1 = pd.Series(range(1880, 2051)) # 2050 tak extend kiya
    plt.plot(years_predict1, res1.intercept + res1.slope * years_predict1, 'r') # 'r' means red color

    # Create second line of best fit (2000-2013, extended to 2050)
    df_recent = df[df['Year'] >= 2000]
    res2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_predict2 = pd.Series(range(2000, 2051)) # 2050 tak extend kiya
    plt.plot(years_predict2, res2.intercept + res2.slope * years_predict2, 'g') # 'g' means green color

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.grid(True) # Optional: grid lines add ki

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

# Agar tum chahte ho ki ye function seedhe run ho jab tum file chalao:
if __name__ == '__main__':
    draw_plot()