import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    #  Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # : Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data', alpha=0.6)

    #  Create first line of best fit (1880 to 2050)
    slope1, intercept1, r1, p1, stderr1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x1 = pd.Series(range(1880, 2051))
    y1 = slope1 * x1 + intercept1
    plt.plot(x1, y1, color='red', label='Best fit line 1880–2050')

    #  Create second line of best fit (from 2000 to 2050)
    df_recent = df[df['Year'] >= 2000]
    slope2, intercept2, r2, p2, stderr2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x2 = pd.Series(range(2000, 2051))
    y2 = slope2 * x2 + intercept2
    plt.plot(x2, y2, color='green', label='Best fit line 2000–2050')

    #  Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()

    #  Save plot and return axis
    plt.savefig('sea_level_plot.png')
    return plt.gca()
