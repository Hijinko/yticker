#!/usr/bin/env python3
from requests import request


class Ticker:
    """
    :brief Stock ticker class
    :param symbol string that is the stock ticker symbol i.e "GME"
    """
    def __init__(self, symbol):
        self._symbol = symbol
        self._url = (
                    "https://query1.finance.yahoo.com/v7/finance/download/"
                    f"{self._symbol}?period1=1598232027&period2=1629768027&"
                    "interval=1d&events=history&includeAdjustedClose=true"
                   )
        self._user_agent = (
                           "Mozilla/5.0 (compatible; Googlebot/2.1;"
                           " +http://www.google.com/bot.html)"
                          )
        self._headers = {"user-agent": self._user_agent}
        self._data = request("GET", self._url, headers=self._headers)\
            .text.split('\n')[1:]
        self._days = {day.split(',')[0]: day.split(',')[1:]
                        for day in self._data}

    @property
    def days(self):
        return self._days

    def stat(self, day):
        fmt = "Open: {:15} High: {:15} Low: {:15} Adj Close: {:15} Volume: {:15}"
        return fmt.format(*self._days[day]) 

    def __repr__(self):
        return str(self._days) 
