class MyAccount:
    def __init__(self, quote_balance=0, base_balance=0, quote_debt=0, base_debt=0, available=0):
        self.quote_balance = quote_balance
        self.base_balance = base_balance
        self.base_debt = base_debt
        self.available = available
