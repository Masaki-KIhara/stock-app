import pandas as pd 
import matplotlib.pyplot as plt
import yfinance as yf
import altair as alt


def get_data(days,tickers):
    df = pd.DataFrame()
    for company in tickers.keys():
        print(company)
        tkr = yf.Ticker(tickers[company])
        hist = tkr.history(period=f"{days}")
        hist.index = hist.index.strftime("%d %B %Y")
        hist = hist[["Close"]]
        hist.columns = [company]
        hist = hist.T
        hist.index.name = "Name"
        hist.head()
        hist = hist.T
        hist.index.name = "Name"
        df = pd.concat([df,hist])
    return df

days = 20
tickers = {
    "apple":"AAPL",
    "facebook":"FB",
    "google":"GOOGL",
    "microsoft":"msft",
    "netflix":"NFLX",
    "amazon":"AMZN"
}

df = get_data(days,tickers)

companies = ["apple","facebook"]
data = df.ilock[companies]
data.sort_index()
data = data.T.reset_index()
data.head()

data = pd.melt(data,id_vars=["Date"]).rename(columns={"value":"Stock Prices(USD)"})
data


ymin,ymax = 250,300 
chart = (
    alt.Chart(data).mark_line(opacity=0.8,clip=True).encode(x = "Date:T",y = alt.Y("Stock Prices(USD):Q",stock=None,scale=alt.Scale(domain=[ymin,ymax])),color="Name:N"
    )
)

chart