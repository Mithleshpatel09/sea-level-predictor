import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 6)) 
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    res1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_predict1 = pd.Series(range(1880, 2051)) 
    plt.plot(years_predict1, res1.intercept + res1.slope * years_predict1, 'r') # 'r' means red color

    # Create second line of best fit (2000-2013, extended to 2050)
    df_recent = df[df['Year'] >= 2000]
    res2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_predict2 = pd.Series(range(2000, 2051)) # 2050 tak extend kiya
    plt.plot(years_predict2, res2.intercept + res2.slope * years_predict2, 'g') 
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.grid(True) 

  
    plt.savefig('sea_level_plot.png')
    return plt.gca()


if __name__ == '__main__':
    draw_plot()