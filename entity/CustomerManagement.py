class Customer:
    def __init__(self, customerID, firstName, lastName, email, phoneNumber):
        self.__customerID = customerID
        self.__firstName = firstName
        self.__lastName = lastName
        self.__email = email
        self.__phoneNumber = phoneNumber

    def get_customerID(self): return self.__customerID
    def set_customerID(self, customerID): self.__customerID = customerID

    def get_firstName(self): return self.__firstName
    def set_firstName(self, firstName): self.__firstName = firstName

    def get_lastName(self): return self.__lastName
    def set_lastName(self, lastName): self.__lastName = lastName

    def get_email(self): return self.__email
    def set_email(self, email): self.__email = email

    def get_phoneNumber(self): return self.__phoneNumber
    def set_phoneNumber(self, phoneNumber): self.__phoneNumber = phoneNumber

    def __repr__(self):
        return (f"Customer ID: {self.__customerID}\n"
                f"First Name: {self.__firstName}\n"
                f"Last Name: {self.__lastName}\n"
                f"Email: {self.__email}\n"
                f"Phone Number: {self.__phoneNumber}")

