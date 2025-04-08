from abc import ABC, abstractmethod
from entity.CarManagement import Vehicle
from entity.CustomerManagement import Customer
from entity.LeaseManagement import Lease
from entity.PaymentHandling import Payment
from datetime import date
class ICarLeaseRepository(ABC):
    
    @abstractmethod
    def addCar(self, car: Vehicle) -> None: ...

    @abstractmethod
    def removeCar(self, car_id: int) -> None: ...

    @abstractmethod
    def listAvailableCars(self) -> list[Vehicle]: ...

    @abstractmethod
    def listRentedCars(self) -> list[Vehicle]: ...

    @abstractmethod
    def findCarById(self, car_id: int) -> Vehicle: ...

    @abstractmethod
    def addCustomer(self, customer: Customer) -> None: ...

    @abstractmethod
    def removeCustomer(self, customer_id: int) -> None: ...

    @abstractmethod
    def listCustomers(self) -> list[Customer]: ...

    @abstractmethod
    def findCustomerById(self, customer_id: int) -> Customer: ...

    @abstractmethod
    def createLease(self, customer_id: int, car_id: int, start_date: date, end_date: date) -> Lease: ...

    @abstractmethod
    def returnCar(self, lease_id: int) -> Lease: ...

    @abstractmethod
    def listActiveLeases(self) -> list[Lease]: ...

    @abstractmethod
    def listLeaseHistory(self) -> list[Lease]: ...

    @abstractmethod
    def recordPayment(self, lease: Lease, amount: float) -> None: ...
