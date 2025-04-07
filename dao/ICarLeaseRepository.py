from abc import ABC, abstractmethod
from entity.CarManagement import Vehicle
from entity.CustomerManagement import Customer
from entity.LeaseManagement import Lease
from entity.PaymentHandling import Payment
from datetime import date
class ICarLeaseRepository(ABC):
    
    @abstractmethod
    def addCar(self, car: Vehicle) -> None:
        pass

    @abstractmethod
    def removeCar(self, car_id: int) -> None:
        pass

    @abstractmethod
    def listAvailableCars(self) -> list[Vehicle]:
        pass

    @abstractmethod
    def listRentedCars(self) -> list[Vehicle]:
        pass

    @abstractmethod
    def findCarById(self, car_id: int) -> Vehicle:
        pass

    @abstractmethod
    def addCustomer(self, customer: Customer) -> None:
        pass

    @abstractmethod
    def removeCustomer(self, customer_id: int) -> None:
        pass

    @abstractmethod
    def listCustomers(self) -> list[Customer]:
        pass

    @abstractmethod
    def findCustomerById(self, customer_id: int) -> Customer:
        pass

    @abstractmethod
    def createLease(self, customer_id: int, car_id: int, start_date: date, end_date: date) -> Lease:
        pass

    @abstractmethod
    def returnCar(self, lease_id: int) -> Lease:
        pass

    @abstractmethod
    def listActiveLeases(self) -> list[Lease]:
        pass

    @abstractmethod
    def listLeaseHistory(self) -> list[Lease]:
        pass

    @abstractmethod
    def recordPayment(self, lease: Lease, amount: float) -> None:
        pass
