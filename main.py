from dao.ICarLeaseRepositoryImpl import ICarLeaseRepositoryImpl
from entity.CarManagement import Vehicle
from entity.CustomerManagement import Customer
from entity.LeaseManagement import Lease
from entity.PaymentHandling import Payment
from datetime import date

def main():
    repo = ICarLeaseRepositoryImpl()  

    while True:
        print("\n==== Car Rental System ====")
        print("1. Add Car")
        print("2. Remove Car")
        print("3. List Available Cars")
        print("4. List Rented Cars")
        print("5. Find Car by ID")
        print("6. Add Customer")
        print("7. Remove Customer")
        print("8. List Customers")
        print("9. Find Customer by ID")
        print("10. Create Lease")
        print("11. Return Car")
        print("12. List Active Leases")
        print("13. List Lease History")
        print("14. Record Payment")
        print("15. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            vehicleID = int(input("Enter car ID: "))
            make = input("Enter make: ")
            model = input("Enter model: ")
            year = input("Enter year(YYYY-MM-DD): ")
            dailyRate = float(input("Enter dailyRate: "))
            passengerCapacity = int(input("Enter PassengerCapacity: "))
            engineCapacity = int(input("Enter EngineCapacity: "))
            car = Vehicle(vehicleID, make, model, year, dailyRate, 1, passengerCapacity, engineCapacity)
            if repo.addCar(car):
                print("Car Added")
            else:
                print("Car is not added")

        
        elif choice == "2":
            car_id = int(input("Enter car ID to remove: "))
            repo.removeCar(car_id)

        elif choice == "3":
            cars = repo.listAvailableCars()
            for car in cars:
                print(car)

        elif choice == "4":
            cars = repo.listRentedCars()
            for car in cars:
                print(car)

        elif choice == "5":
            car_id = int(input("Enter car ID: "))
            car = repo.findCarById(car_id)
            print(car)

        elif choice == "6":
            cust_id = int(input("Enter customer ID: "))
            first = input("First name: ")
            last = input("Last name: ")
            email = input("Email: ")
            phone = input("Phone number: ")
            cust = Customer(cust_id, first, last, email, phone)
            repo.addCustomer(cust)

        elif choice == "7":
            cust_id = int(input("Enter customer ID to remove: "))
            repo.removeCustomer(cust_id)

        elif choice == "8":
            customers = repo.listCustomers()
            for cust in customers:
                print(cust)

        elif choice == "9":
            cust_id = int(input("Enter customer ID: "))
            cust = repo.findCustomerById(cust_id)
            print(cust)

        elif choice == "10":
            cust_id = int(input("Enter customer ID: "))
            car_id = int(input("Enter car ID: "))
            start = input("Enter start date (YYYY-MM-DD): ")
            end = input("Enter end date (YYYY-MM-DD): ")
            lease = repo.createLease(cust_id, car_id, date.fromisoformat(start), date.fromisoformat(end))
            print(lease)

        elif choice == "11":
            lease_id = int(input("Enter lease ID: "))
            lease = repo.returnCar(lease_id)
            print("Car returned:", lease)

        elif choice == "12":
            leases = repo.listActiveLeases()
            for lease in leases:
                print(lease)

        elif choice == "13":
            leases = repo.listLeaseHistory()
            for lease in leases:
                print(lease)

        elif choice == "14":
            lease_id = int(input("Enter lease ID: "))
            amount = float(input("Enter payment amount: "))
            payment = Payment(None, lease_id, amount, date.today())
            repo.recordPayment(payment, amount)

        elif choice == "0":
            print("Thank You for Visiting\n")
            print("Exiting system...")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
