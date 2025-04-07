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
                print("Car Added Successfully")
            else:
                print("Error in adding a car")

        
        elif choice == "2":
            car_id = int(input("Enter car ID to remove: "))
            if repo.removeCar(car_id):
                print("Car Removed Successfully")
            else:
                print("Error in removing a car")
            

        elif choice == "3":
            cars = repo.listAvailableCars()
            for car in cars:
                print("-" * 30)
                print(car)
                

        elif choice == "4":
            cars = repo.listRentedCars()
            for car in cars:
                print("-" * 30)
                print(car)
                

        elif choice == "5":
            car_id = int(input("Enter car ID: "))
            car = repo.findCarById(car_id)
            if car:
                print("-" * 30)
                print(car)
            else:
                print("Car with id: ", car_id, "not found")


        elif choice == "6":
            cust_id = int(input("Enter customer ID: "))
            first = input("First name: ")
            last = input("Last name: ")
            email = input("Email: ")
            phone = input("Phone number: ")
            cust = Customer(cust_id, first, last, email, phone)
            if repo.addCustomer(cust):
                print("Customer added successfully")
            else:
                print("Error in adding customer")


        elif choice == "7":
            cust_id = int(input("Enter customer ID to remove: "))
            if repo.removeCustomer(cust_id):
                print("Customer removed successfully")
            else:
                print("Error in removing customer")


        elif choice == "8":
            customers = repo.listCustomers()
            for customer in customers:
                print("-" * 30)
                print(customer)

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

        elif choice == "15":
            print("Thank You for Visiting\n")
            print("Exiting system...")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
