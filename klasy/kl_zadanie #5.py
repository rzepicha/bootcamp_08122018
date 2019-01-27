class CashMachine:
    #is_available=False
    def __init__(self):
        self._money=[]



    @property
    def is_available (self):
        if self._money:
            return True
        else:
            return False

    def put_money(self, bills_list):
        self._money.extend(bills_list)

    def withdraw_money(self,amount):
        money_to_withdraw=[]
        for bill in sorted(self._money, reverse=True):
            if sum(money_to_withdraw)+bill<=amount:
                money_to_withdraw.append(bill)

        if sum(money_to_withdraw)!=amount:
            return []

        for bill in money_to_withdraw:
            self._money.remove(bill)

        return money_to_withdraw





def test_cash_machine_is_not_available():
    cash_machine=CashMachine()
    assert not cash_machine.is_available

def test_cash_machine_put_money():
    cash_machine=CashMachine()
    cash_machine.put_money([200,100,100,50])
    assert cash_machine.is_available

def test_cash_machine_withdraw_money():
    cash_machine=CashMachine()
    cash_machine.put_money([200,100,100,50])
    assert cash_machine.withdraw_money(150)==[100,50]
    assert cash_machine.withdraw_money(150)==[]