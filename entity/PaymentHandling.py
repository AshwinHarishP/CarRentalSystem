class Payment:
    def __init__(self, paymentID, leaseID, paymentDate, amount):
        self.__paymentID = paymentID
        self.__leaseID = leaseID
        self.__paymentDate = paymentDate
        self.__amount = amount
        
    def get_paymentID(self): return self.__paymentID
    def set_paymentID(self, paymentID): self.__paymentID = paymentID

    def get_leaseID(self): return self.__leaseID
    def set_leaseID(self, leaseID): self.__leaseID = leaseID

    def get_paymentDate(self): return self.__paymentDate
    def set_paymentDate(self, paymentDate): self.__paymentDate = paymentDate

    def get_amount(self): return self.__amount
    def set_amount(self, amount): self.__amount = amount