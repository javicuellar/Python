# Proyecto recogido del repositorio de edmoor - Stock-Market-Alerts-with-Twilio
#    Link: https://github.com/edmoor/Stock-Market-Alerts-with-Twilio

import requests
from twilio.rest import Client



# Configuración de las API y credenciales
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
API_KEY_STOCK = "XXXXX"
FUNCTION = "TIME_SERIES_DAILY"
API_KEY_NEWS = "XXXXX"

# Credenciales de Twilio
TWILIO_CODE = "XXXX"
SID = "XXXXXX"
API_KEY_TWILIO = "XXXXXXX"
TWILIO_DEVICE = "XXXXX"
MY_PHONE = "XXXXXX"
client = Client(SID, API_KEY_TWILIO)



url_stock = f'{STOCK_ENDPOINT}?function={FUNCTION}&symbol={STOCK_NAME}&apikey={API_KEY_STOCK}'
r_stock = requests.get(url_stock)
data_stock = r_stock.json()

if "Error Message" in data_stock:
    print("Error in API call:", data_stock["Error Message"])
elif "Note" in data_stock:
    print("API call limit reached:", data_stock["Note"])
else:
    time_series = data_stock["Time Series (Daily)"]
    dates = list(time_series.keys())
    yesterday = dates[0]
    day_before_yesterday = dates[1]
    yesterday_close = float(time_series[yesterday]['4. close'])
    day_before_yesterday_close = float(time_series[day_before_yesterday]['4. close'])
    percentage_change = ((yesterday_close - day_before_yesterday_close) / day_before_yesterday_close) * 100

    print(f"Yesterday's close: {yesterday_close}")
    print(f"Day before yesterday's close: {day_before_yesterday_close}")
    print(f"Percentage change: {percentage_change:.2f}%")

if abs(percentage_change) >= 5:
        url_news = f"{NEWS_ENDPOINT}?q={COMPANY_NAME}&from=2024-05-14&sortBy=publishedAt&apiKey={API_KEY_NEWS}"
        r_news = requests.get(url_news)
        data_news = r_news.json()
        
        if "articles" in data_news:
            articles = data_news["articles"]
            articles_list = [(article['title'], article['description']) for article in articles[:3]]

            for title, description in articles_list:
                message = client.messages.create(
                    body=f"Title: {title}\nDescription: {description}",
                    from_=TWILIO_DEVICE,
                    to=MY_PHONE
                )
                print(f"Sent message: {message.sid}")
        else:
            print("No articles found or error in fetching news.")


