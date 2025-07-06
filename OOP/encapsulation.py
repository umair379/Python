class Umair:
    def __init__(self, bank , account):
        self.bank = bank
        self.__account = account #private

    def get_account(self):
        return self.__account

umair = Umair("meezan" , 3637276635524251)
# print(umair.__account) # print nahi hoga kyunki ye private hai
print(umair.get_account())
print(umair._Umair__account)