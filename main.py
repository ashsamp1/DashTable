import dash
import dash_table
import pandas as pd

df = pd.read_csv('https://api.covid19india.org/csv/latest/state_wise.csv')
bootstrap = "https://stackpath.bootstrapcdn.com/bootswatch/4.5.2/solar/bootstrap.min.css"
app = dash.Dash(__name__, external_stylesheets=[bootstrap])

app.layout = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records'),
)

if __name__ == '__main__':
    app.run_server(debug=True)