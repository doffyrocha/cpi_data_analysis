import requests
import pandas as pd

def fetch_cpi_data():
    url = "https://api.bls.gov/publicAPI/v2/timeseries/data/"
    headers = {"Content-Type": "application/json"}
    data = {
        "seriesid": ["CUUR0000SA0", "CUUR0000SA0L1E", "CUUR0000SETB01"],
        "startyear": "2019",
        "endyear": "2024",
        "registrationkey": "642b075d082641308c724eae5437a033"
    }
    response = requests.post(url, json=data, headers=headers)
    json_data = response.json()

    series_data = {}
    for series in json_data['Results']['series']:
        series_id = series['seriesID']
        series_data[series_id] = []
        for item in series['data']:
            year = item['year']
            period = item['period']
            value = float(item['value'])
            series_data[series_id].append((year, period, value))

    df = pd.DataFrame(series_data["CUUR0000SA0"], columns=["Year", "Period", "CPI_ALL_Items"])
    df["CPI_Less_Food_Energy"] = [x[2] for x in series_data["CUUR0000SA0L1E"]]
    df["CPI_Gasoline"] = [x[2] for x in series_data["CUUR0000SETB01"]]
    df.to_csv("cpi_data.csv", index=False)

if __name__ == "__main__":
    fetch_cpi_data()
