from custom_modules import messages as m
from custom_modules import stock_data as s
from custom_modules import finviz as f
from custom_modules import more_stock_data as z
from custom_modules import investors_hub as ih
class Scraper:
    def symbol_getter(self):
        self.symbol = input("Enter stock symbol: ")

    def scrape_yahoo(self):
        yahoo = s.YahooFinance(self.symbol)
        yahoo.build_url()
        yahoo.parser()
        yahoo.pull_table_data()


    def scrape_stock_twits(self):
        user = m.StockTwits(self.symbol)
        user.open_parser()
        user.find_element()
        user.display()

    def scrape_finviz(self):
        fin = f.FinViz(self.symbol)
        fin.build_url()
        fin.parser()
        fin.pull_table_data()

    def more_yahoo_finance(self):
        more = z.MoreYahooFinance(self.symbol)
        more.build_url()
        more.parser()
        more.pull_table_data()

    def investors_hub(self):
        stocks = ih.InvestorsHub()
        stocks.pull()
        stocks.filter_results()
        self.potential_stocks = stocks.results()
        print(self.potential_stocks)



scraper = Scraper()
scraper.investors_hub()
print(" ", '\n')
scraper.symbol_getter()
print("  ")
scraper.scrape_yahoo()
print("   ")
scraper.more_yahoo_finance()
print("   ")
scraper.scrape_stock_twits()
print("   ")
scraper.scrape_finviz()
