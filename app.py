from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server  # 提供 Flask WSGI 物件給 Gunicorn

# 示例 Dash 佈局
df = pd.DataFrame({
    "Category": ["A", "B", "C"],
    "Values": [10, 20, 15]
})
fig = px.bar(df, x="Category", y="Values", title="Benson Kong Power Dashboard")

app.layout = html.Div([
    html.H1("Benson Kong Power Dashboard"),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=5000, debug=False)
