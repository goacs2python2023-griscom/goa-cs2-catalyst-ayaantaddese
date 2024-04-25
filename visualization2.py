import pandas as pd
import numpy as np
from bokeh.plotting import figure, show
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, HoverTool, Div, Toggle
from bokeh.models.callbacks import CustomJS

df = pd.read_csv("visualization2_data_generator.csv", header=None, names=["Country", "GDP", "Connections"])
df['GDP'] = pd.to_numeric(df['GDP'], errors='coerce')
df['Connections'] = pd.to_numeric(df['Connections'], errors='coerce')
df = df.dropna(subset=['GDP', 'Connections'])

source = ColumnDataSource(df)
p = figure(title="GDP of a Nation vs Nations Connected to With a Direct Flight", x_axis_type="log", width=700, height=400)
p.xaxis.axis_label, p.yaxis.axis_label, p.y_range.start, p.y_range.end, p.title.align = 'GDP in USD (log scale)', 'Nations Connected to With a Direct Flight', 0, 100, 'center'

p.circle(x='GDP', y='Connections', size=10, color='blue', alpha=0.6, source=source)

hover = HoverTool(tooltips=[("Country", "@Country"), ("GDP", "@GDP"), ("Connections", "@Connections")])
p.add_tools(hover)

x = df['GDP']
y = df['Connections']
log_x = np.log10(x)
log_y = np.log10(y)

coeffs = np.polyfit(log_x, log_y, 1)
a = coeffs[0]
b = 10**coeffs[1]

trendline_x = np.linspace(min(x), max(x), 100)
trendline_y = b * (trendline_x ** a)
trendline = p.line(trendline_x, trendline_y, line_width=2, color='red')

y_pred = b * (x ** a)
ss_res = np.sum((y - y_pred) ** 2)
y_mean = np.mean(y)
ss_tot = np.sum((y - y_mean) ** 2)
r2 = 1 - (ss_res / ss_tot)

info_div = Div(text=f"<b>Trendline Equation:</b> y = {b:.2e} * x^{a:.2f}<br><b>Trendline R^2 Value:</b> {r2:.4f}", styles={"text-align": "left"})
toggle_button = Toggle(label="Toggle Trendline", button_type="success", active=True)

toggle_callback = CustomJS(args={"trendline": trendline}, code="trendline.visible = this.active;")
toggle_button.js_on_change("active", toggle_callback)

layout = column(p, info_div, toggle_button)
show(layout)
