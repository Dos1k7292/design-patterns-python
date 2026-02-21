import copy


class Discount:

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def clone(self):
        return copy.deepcopy(self)
