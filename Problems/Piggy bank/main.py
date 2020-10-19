class PiggyBank:
    dollars = 0
    cents = 0

    # create __init__ and add_money methods
    def __init__(self, dollars, cents):
        PiggyBank.dollars = dollars
        PiggyBank.cents = cents

    def add_money(self, deposit_dollars, deposit_cents):
        self.dollars += deposit_dollars
        self.cents += deposit_cents
        if self.cents > 99:
            self.dollars += self.cents // 100
            self.cents = self.cents % 100


# my_bank = PiggyBank(1, 1)
#
# my_bank.add_money(0, 99)
#
# print(my_bank.dollars, my_bank.cents)
