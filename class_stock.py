import random
import csv


class Stock:
    def __init__(
            self,
            stock_price: float,
            shares_outstanding: int,
            market_cap: float,
            earnings: float,
            eps: float,
            pe_ratio: float,
            payout_rate: int,
            dividend: float,
            dividend_yield: float,
            num_of_transactions: [],
            price_history: [],
            all_data: [],
    ):

        self.stock_price = stock_price
        self.shares_outstanding = shares_outstanding
        self.market_cap = market_cap
        self.earnings = earnings
        self.eps = eps
        self.pe_ratio = pe_ratio
        self.payout_rate = payout_rate
        self.dividend = dividend
        self.dividend_yield = dividend_yield
        self.num_of_transactions = num_of_transactions
        self.price_history = price_history
        self.all_data = all_data

    def update_stock(self, change_rate):
        """Updates Stock 'stock_price', 'market_cap', 'pe_ratio', 'dividend_yield' parameters."""

        # Updating Stock 'self.stock_price' parameter using 'change_rate' argument:
        self.stock_price = float(self.stock_price * change_rate)
        self.stock_price = round(self.stock_price, 2)

        # Updating Stock 'self.market_cap' parameter:
        self.market_cap = self.stock_price * self.shares_outstanding
        self.market_cap = round(self.stock_price, 2)

        # Updating Stock 'self.pe_ratio' parameter:
        self.pe_ratio = self.stock_price / self.eps
        self.pe_ratio = round(self.pe_ratio, 2)

        # Updating Stock 'self.dividend_yield' parameter:
        self.dividend_yield = (self.dividend * 100) / self.stock_price
        self.dividend_yield = round(self.dividend_yield, 2)

        # Updating 'self.price_history' list:
        self.price_history.append(self.stock_price)

        # Updating 'self.num_of_transactions' list:
        transaction_num = len(self.price_history)
        self.num_of_transactions.append(transaction_num)

        # Updating 'self.all_data' list:
        last_stock_price = [self.num_of_transactions[-1], self.price_history[-1]]
        self.all_data.append(last_stock_price)

        return \
            self.stock_price, \
            self.market_cap, \
            self.pe_ratio, \
            self.dividend_yield, \
            self.num_of_transactions, \
            self.price_history, \
            self.all_data

    def w_data_csv(self):
        """Creates .csv file 'Stock.all_data' and adds 'all_data' parameter to the file."""

        file_header = [
            "No.",
            "Stock Price"
        ]

        with open('Stock.all_data.csv', 'w+', newline='') as stk_info:
            csv_w = csv.writer(stk_info)
            csv_w.writerow(file_header)
            csv_w.writerows(self.all_data)

    def mkt_high_grow(self):
        """Initiating highest grow market.
        Recommending to use when P/E ratio is between 12 and 18."""

        change_rate = round(random.uniform(0.9997, 1.0012), 4)
        self.update_stock(change_rate)
        self.w_data_csv()

    def mkt_modest_grow(self):
        """Initiating modest grow market.
        Recommending to use when P/E ratio is between 18 and 19."""

        change_rate = round(random.uniform(0.9997, 1.0009), 4)
        self.update_stock(change_rate)
        self.w_data_csv()

    def mkt_low_grow(self):
        """Initiating low grow market.
        Recommending to use when P/E ratio is between 19 and 21."""

        change_rate = round(random.uniform(0.9997, 1.0005), 4)
        self.update_stock(change_rate)
        self.w_data_csv()

    def mkt_correction(self):
        """Initiating Correction - prices goes drastically down, and barely climbs up.
        The only way to exit function is when 'self.pe_ratio' parameter becomes lesser than 5."""

        while self.pe_ratio > 5:
            change_rate = round(random.uniform(0.91, 1.05), 2)
            self.update_stock(change_rate)
            self.w_data_csv()

    def mkt_bear(self):
        """Initiating Bear market - prices goes down, and barely climbs up."""

        change_rate = round(random.uniform(0.89, 1.05), 2)
        self.update_stock(change_rate)
        self.w_data_csv()

    def mkt_bull(self):
        """Initiating Bull market - prices climbs up, and barely goes down."""

        change_rate = round(random.uniform(0.9999, 1.0025), 4)
        self.update_stock(change_rate)
        self.w_data_csv()
