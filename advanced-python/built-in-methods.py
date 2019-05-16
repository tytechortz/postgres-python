class Currency:
    def __init__(self, code, exchange_to_usd):
        self.amount = 0.00
        self.code = code
        self.exchange_to_usd = exchange_to_usd

    def set_amount(self, amount):
        self.amount = amount

    def in_currency(self, amount):
        return amount / self.exchange_to_usd

    def to_usd(self, amount=None):
        return amount * self.exchange_to_usd


pounds = Currency("GBP", 1.21)
print(pounds.to_usd(1000))