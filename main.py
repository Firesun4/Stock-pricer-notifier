import finnhub
import time

from numpy import diff
class stockInfoNotifier():
    def __init__(self):
        self.stock_price_info = finnhub.Client(api_key="cap9qpiad3iahju4e32g")
    def priceChangeLoop(self,ticker):
        stock_price_info = finnhub.Client(api_key="cap9qpiad3iahju4e32g")
        self.currentPrice = stock_price_info.quote(ticker).get("c")
        while(abs(self.currentPrice-self.initial)<self.dif):
            print(abs(self.currentPrice-self.initial))
            stock_price_info = finnhub.Client(api_key="cap9qpiad3iahju4e32g")
            self.currentPrice = stock_price_info.quote(ticker).get("c")
            print(self.currentPrice)
            time.sleep(1)
    def alert(self, ticker, dif):
        self.dif = dif
        self.stock_quote = self.stock_price_info.quote(ticker)
        self.initial = self.stock_price_info.quote(ticker).get("c")
        print(self.initial)
        self.priceChangeLoop(ticker)
        print("THE PRICE DIFFERENCE HAS BEEN MET")

a = stockInfoNotifier()
a.alert(input("Ticker: "), float(input("Difference: ")))
        
    

