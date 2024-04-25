from bokeh.plotting import figure, show
from bokeh.models import HoverTool, ColumnDataSource, Div
from bokeh.transform import linear_cmap
from bokeh.palettes import Spectral6
from bokeh.layouts import column
import pandas as pd

df = pd.read_csv("visualization1_data_generator.csv")
df_sorted = df.sort_values(by='Connections', ascending=False)
top_100_df, top_10_df = df_sorted.head(100), df_sorted.head(10)

source_top_100 = ColumnDataSource(top_100_df)
p = figure(title="Top 100 Most Connected Country Pairs vs. Average GDP per Capita", x_axis_label="Average GDP per Capita (USD)", y_axis_label="Number of Connections (direct flights)", width=700, height=400)

p.scatter(x='Average GDP per Capita', y='Connections', source=source_top_100, size=10, color=linear_cmap('Connections', palette=Spectral6, low=min(top_100_df['Connections']), high=max(top_100_df['Connections'])), alpha=0.7)

hover = HoverTool(tooltips=[("Countries", "@Countries"), ("Average GDP per Capita", "@{Average GDP per Capita} USD"), ("Connections", "@Connections")])
p.add_tools(hover)

top_10_list = "<b>Top 10 Most Connected Countries:</b><br><ul>"
top_10_list += ''.join(f"<li>{row['Countries']}: {row['Connections']} connections</li>" for _, row in top_10_df.iterrows())
top_10_list += "</ul>"

top_10_div = Div(text=top_10_list, width=700, height=100)
layout = column(p, top_10_div)
show(layout)
