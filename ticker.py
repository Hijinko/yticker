from requests import request

class Ticker:
    def __init__(self, symbol):
        self.symbol = symbol
        self.url = f"https://query1.finance.yahoo.com/v7/finance/download/{self.symbol}?period1=1598232027&period2=1629768027&interval=1d&events=history&includeAdjustedClose=true"
        self.user_agent = "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
        self.headers = {"user-agent": self.user_agent}
        self.data = request("GET", self.url, headers=self.headers).text.split('\n')[1:]
        self.history = {day.split(',')[0]: day.split(',')[1:] for day in self.data}
    
    def get_day(self, day):
        return self.history[day]
