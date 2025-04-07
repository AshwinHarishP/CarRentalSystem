class Vehicle:
    def __init__(self, vehicleID, make, model, year, dailyRate, status, passengerCapacity, engineCapacity):
        self.__vehicleID = vehicleID
        self.__make = make
        self.__model = model
        self.__year = year
        self.__dailyRate = dailyRate
        self.__status = status
        self.__passengerCapacity = passengerCapacity
        self.__engineCapacity = engineCapacity


    def get_vehicleID(self): return self.__vehicleID 
    def set_vehicleID(self, vehicleID): self.__vehicleID = vehicleID
    
    def get_make(self): return self.__make
    def set_make(self, make): self.__make = make

    def get_model(self): return self.__model
    def set_model(self, model): self.__model = model

    def get_year(self): return self.__year
    def set_year(self, year): self.__year = year

    def get_dailyRate(self): return self.__dailyRate
    def set_dailyRate(self, daily_rate): self.__dailyRate = dailyRate

    def get_status(self): return self.__status
    def set_status(self, status): self.__status = status

    def get_passengerCapacity(self): return self.__passengerCapacity
    def set_passengerCapacity(self, passengerCapacity): self.__passengerCapacity = passengerCapacity

    def get_engineCapacity(self): return self.__engineCapacity
    def set_engineCapacity(self, engineCapacity): self.__engineCapacity = engineCapacity
    
