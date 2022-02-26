from numpy import datetime64
from payment import Payment

class Card(Payment):
    number = int
    CVV_number = int
    date = datetime64

    def __init__(self, id, number, CVV_number, date):
        super().__init__(id)
        self.number = number
        self.CVV_number = CVV_number
        self.date = date

