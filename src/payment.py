class Payment:
    def __init__(self, amount):
        self.amount = amount

    def process_payment(self):
        return f"Payment of R{self.amount} successful"