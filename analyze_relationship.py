import pandas as pd

def analyze_relationship():
    df = pd.read_csv("cpi_data.csv")
    correlation = df["CPI_ALL_Items"].corr(df["CPI_Gasoline"])
    print(f"Correlação entre CPI All Items e CPI Gasoline: {correlation}")

if __name__ == "__main__":
    analyze_relationship()
