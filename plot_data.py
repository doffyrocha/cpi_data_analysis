import pandas as pd
import plotly.express as px

def plot_cpi_data():
    df = pd.read_csv("cpi_data.csv")
    df['Date'] = pd.to_datetime(df['Year'].astype(str) + df['Period'].str.replace('M', ''), format='%Y%m')
    df.set_index('Date', inplace=True)
    
    df['YoY Change'] = df['CPI_Less_Food_Energy'].pct_change(12) * 100

    fig = px.line(df, x=df.index, y="YoY Change", title="CPI Less Food and Energy (YoY % Change)")
    fig.update_xaxes(rangeslider_visible=True)
    fig.show()

if __name__ == "__main__":
    plot_cpi_data()
