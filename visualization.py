import pandas as pd
from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.transform import factor_cmap
from scipy.optimize import curve_fit
import numpy as np
from bokeh.models import Label

# Load datasets
connections_data = pd.read_csv("connections.txt", delimiter=":", header=None, names=["Countries", "Connections"])
gdp_data = pd.read_csv("gdp_data.csv")

# Split Countries and Connections
connections_data[['Country1', 'Country2']] = connections_data['Countries'].str.split('+', expand=True)

# Calculate average GDP for each connection
connections_data['Average_GDP'] = connections_data.apply(lambda row: 
                                                         (gdp_data.loc[gdp_data['Country'] == row['Country1']]['GDP per Capita'].values[0] + 
                                                          gdp_data.loc[gdp_data['Country'] == row['Country2']]['GDP per Capita'].values[0]) / 2, 
                                                         axis=1)

# Convert connections to numeric
connections_data['Connections'] = connections_data['Connections'].str.strip().astype(int)

# Bokeh plot
output_file("scatterplot.html")

# Create a figure
p = figure(title="GDP vs Connections", x_axis_label='Average GDP', y_axis_label='Connections', tools="", toolbar_location=None)

# Data source
source = ColumnDataSource(connections_data)

# Scatter plot
p.circle(x='Average_GDP', y='Connections', source=source, size=10, color="navy", alpha=0.5)

# Exponential trendline
def exponential_func(x, a, b, c):
    return a * np.exp(b * x) + c

popt, _ = curve_fit(exponential_func, connections_data['Average_GDP'], connections_data['Connections'])

x = np.linspace(connections_data['Average_GDP'].min(), connections_data['Average_GDP'].max(), 100)
y = exponential_func(x, *popt)

p.line(x, y, line_width=2, color="red")

# Calculate r^2
residuals = connections_data['Connections'] - exponential_func(connections_data['Average_GDP'], *popt)
ss_res = np.sum(residuals**2)
ss_tot = np.sum((connections_data['Connections'] - np.mean(connections_data['Connections']))**2)
r_squared = 1 - (ss_res / ss_tot)

# Add equation and r^2 value to the plot
label = Label(x=0.1, y=300, text=f'y = {popt[0]:.2f} * exp({popt[1]:.2f} * x) + {popt[2]:.2f}, R^2 = {r_squared:.2f}', 
              render_mode='css', text_font_size='10pt')
p.add_layout(label)

# Hover tool
hover = HoverTool()
hover.tooltips = [("Countries", "@Country1 and @Country2"),
                  ("Connections", "@Connections"),
                  ("Average GDP", "@Average_GDP")]
p.add_tools(hover)

# Show plot
show(p)
