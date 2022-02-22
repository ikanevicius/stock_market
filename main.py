import random
# import time
import class_stock as stc


def create_stock():
    """Creates and returns new 'Stock' class."""

    # Creates initial stock price:
    price = float(random.uniform(0.27, 135))
    price = round(price, 2)

    # Creates number of shares outstanding and counts market cap:
    shares = random.randint(1000000, 1000000000)
    mkt_cap = price * shares

    # Creates P/E ratio which is used to create earnings parameters:
    pe_ratio = float(random.uniform(12, 18))
    pe_ratio = round(pe_ratio, 1)

    earnings = mkt_cap / pe_ratio
    eps = earnings / shares
    eps = round(eps, 2)

    # Creates payout rate, which is used to create dividend parameters:
    pay_rate = int(random.randint(25, 75))
    dividend = (eps * pay_rate) / 100
    dividend = round(dividend, 2)

    dividend_yield = (dividend * 100) / price
    dividend_yield = round(dividend_yield, 2)

    # Creates empty list that will be used to create list parameters:
    empty_list_1 = []
    empty_list_2 = []
    empty_list_3 = []

    # Creating new 'Stock" class:
    stock_created = stc.Stock(
        price,
        shares,
        mkt_cap,
        earnings,
        eps,
        pe_ratio,
        pay_rate,
        dividend,
        dividend_yield,
        empty_list_1,
        empty_list_2,
        empty_list_3,
    )

    return stock_created


def stock_info(share):
    print(f"""___
Price: {share.stock_price}€
P/E ratio: {share.pe_ratio}

EPS: {share.eps}€
Dividend: {share.dividend}€
Yield: {share.dividend_yield}%""")


def print_info(share):
    print(f"""
{share.stock_price}
{share.pe_ratio}""")


share_1 = create_stock()
stock_info(share_1)


def invisible_hand(share):
    if share.pe_ratio < 12:
        num = random.randint(1, 75)
        if num == 1:
            share.mkt_bear()
        else:
            share.mkt_bull()
            print_info(share)

    if 12 <= share.pe_ratio <= 18:
        num = random.randint(1, 50)
        if num == 1:
            share.mkt_bear()
        else:
            share.mkt_high_grow()
            print_info(share)

    if 18 < share.pe_ratio <= 19:
        num = random.randint(1, 45)
        if num == 1:
            share.mkt_bear()
        else:
            share.mkt_modest_grow()
            print_info(share)

    if 19 < share.pe_ratio <= 21:
        num = random.randint(1, 40)
        if num == 1:
            share.mkt_bear()
        else:
            share.mkt_low_grow()
            print_info(share)

    if share.pe_ratio > 21:
        share.mkt_correction()
        print_info(share)


while True:
    # TODO: Time Change parameter:
    # time.sleep(0)
    invisible_hand(share_1)
