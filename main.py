from dao.ICarLeaseRepositoryImpl import ICarLeaseRepositoryImpl
from entity.CarManagement import Vehicle
from entity.CustomerManagement import Customer
from entity.LeaseManagement import Lease
from entity.PaymentHandling import Payment
from myexceptions.CarNotFoundException import CarNotFoundException
from myexceptions.LeaseNotFoundException import LeaseNotFoundException
from myexceptions.CustomerNotFoundException import CustomerNotFoundException
from datetime import date

class CarRentalSystem:
    def __init__(self):
        self.repo = ICarLeaseRepositoryImpl()
    
    def displayMenu(self):
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
            print("11. Return Car based on Lease ID")
            print("12. List Active Leases")
            print("13. List Lease History")
            print("14. Find Lease by Lease ID")
            print("15. Record Payment")
            print("16. Exit")

    def main(self): 
        self.displayMenu()

        while True:
            
            choice = input("\nEnter your choice: ")

            if choice == "1":
                print("\nAdd Car\n")
                vehicleID = int(input("Enter car ID: "))
                make = input("Enter make: ")
                model = input("Enter model: ")
                year = input("Enter year(YYYY-MM-DD): ")
                dailyRate = float(input("Enter dailyRate: "))
                passengerCapacity = int(input("Enter PassengerCapacity: "))
                engineCapacity = int(input("Enter EngineCapacity: "))
                car = Vehicle(vehicleID, make, model, year, dailyRate, 1, passengerCapacity, engineCapacity)
                
                if self.repo.addCar(car):
                    print("Car Added Successfully")
                else:
                    print("Error in adding a car")

            
            elif choice == "2":
                print("\nRemove Car\n")
                
                try:
                    car_id = int(input("Enter car ID to remove: "))

                    if not self.repo.findCarById(car_id):
                        raise CarNotFoundException(f"Car with ID {car_id} does not exist.")

                    if self.repo.removeCar(car_id):
                        print("Car Removed Successfully")
                    else:
                        print("Error in removing a car")

                except CarNotFoundException as Error:
                    print(f"Error in removing a car: {Error}")
                

            elif choice == "3":
                print("\nList All Available Cars\n")
                cars = self.repo.listAvailableCars()
                for car in cars:
                    print("-" * 30)
                    print(car)
                    

            elif choice == "4":
                print("\nList Rented Cars\n")
                cars = self.repo.listRentedCars()
                for car in cars:
                    print("-" * 30)
                    print(car)
                    

            elif choice == "5":
                print("\nFind Car by Car ID\n")
                
                try:
                    car_id = int(input("Enter car ID: "))
                    car = self.repo.findCarById(car_id)
                    if not car:
                        raise CarNotFoundException(f"Car with ID {car_id} does not exist.")
                    
                    else:
                        print("-" * 30)
                        print(car)
                
                except CarNotFoundException as Error:
                    print(f"Error in finding a car: {Error}")

            elif choice == "6":
                print("\nAdd Customer\n")

                try:

                    cust_id = int(input("Enter customer ID: "))
                    if self.repo.findCustomerById(cust_id):
                        raise CustomerNotFoundException(f"Customer with ID {cust_id} already exist.")
                    
                    else:
                        first = input("First name: ")
                        last = input("Last name: ")
                        email = input("Email: ")
                        phone = input("Phone number: ")
                        cust = Customer(cust_id, first, last, email, phone)
                        if self.repo.addCustomer(cust):
                            print("Customer added successfully")
                        else:
                            print("Error in adding customer")

                except CustomerNotFoundException as Error:
                    print(f"Error in adding a : {Error}")


            elif choice == "7":
                print("\nRemove Customer\n")
                
                try:
                    cust_id = int(input("Enter customer ID to remove: "))
                
                    if not self.repo.findCustomerById(cust_id):
                        raise CustomerNotFoundException(f"Customer with ID {cust_id} does not exist.") 

                    if self.repo.removeCustomer(cust_id):
                        print("Customer removed successfully")
                    else:
                        print("Error in removing customer")

                except CustomerNotFoundException as Error:
                    print(f"Error in removing a customer: {Error}")


            elif choice == "8":
                print("\nList of Customers\n")
                customers = self.repo.listCustomers()
                for customer in customers:
                    print("-" * 30)
                    print(customer)


            elif choice == "9":
                print("\nFind Customer by Customer ID\n")

                try:
                    cust_id = int(input("Enter customer ID: "))
                    if not self.repo.findCustomerById(cust_id):
                        raise CustomerNotFoundException(f"Customer with ID {cust_id} does not exist.")  

                    customer = self.repo.findCustomerById(cust_id)
                    print(customer)

                except CustomerNotFoundException as Error:
                    print(f"Error in finding a customer: {Error}")


            elif choice == "10":
                print("\nCreate Lease\n")
                try:

                    customer_id = int(input("Enter customer ID: "))
                    car_id = int(input("Enter car ID: "))

                    if not self.repo.findCustomerById(customer_id):
                        raise CustomerNotFoundException(f"Customer with ID {customer_id} does not exist.")

                    if not self.repo.findCarById(car_id):
                        raise CarNotFoundException(f"Car with ID {car_id} does not exist.")
                
                    else:
                        start = input("Enter start date (YYYY-MM-DD): ")
                        end = input("Enter end date (YYYY-MM-DD): ")
                        print(" \n1. Monthy Lease \n2. Daily Lease")
                        leaseInput = input("Enter Lease Type: ")
                    
                        if leaseInput == "1":
                            leaseType = "Monthly Lease"
                        else:
                            leaseType = "Daily Lease"

                        lease = self.repo.createLease(customer_id, car_id, date.fromisoformat(start), date.fromisoformat(end), leaseType)
                        if lease:
                            print("Lease Created Successfully")
                        else:
                            print("Error in creating a lease")
                
                except CustomerNotFoundException as Error:
                    print(f"Error in finding a customer: {Error}")
                
                except CarNotFoundException as Error:
                    print(f"Error in finding a car: {Error}")


            elif choice == "11":
                print("\nReturn a Car based on Lease ID\n")

                try:
                    lease_id = int(input("Enter lease ID: "))
                    lease, vehicle = self.repo.returnCar(lease_id)

                    if lease:
                        print("\n\nLease Details\n")
                        print("Lease ID:", lease.get_leaseID())
                        print("Vehicle ID:", lease.get_vehicleID())
                        print("Customer ID:", lease.get_customerID())
                        print("Start Date:", lease.get_startDate())
                        print("End Date:", lease.get_endDate())
                        print("Lease Type:", lease.get_type())
                        
                        print("\n\nVehicle Info\n")
                        print("Make:", vehicle["make"])
                        print("Model:", vehicle["model"])
                        print("Year:", vehicle["year"])
                    elif not lease:
                        raise LeaseNotFoundException(f"Lease with ID {lease_id} does not exist.")
                    
                    else:
                        raise CustomerNotFoundException(f"Customer with ID {cust_id} does not exist.") 
            

                except LeaseNotFoundException as Error:
                    print(f"Error in returning a lease based on lease ID {lease_id}: {Error}")
                    
                
                except CustomerNotFoundException as Error:
                    print(f"Error in finding a customer: {Error}")


            elif choice == "12":
                print("\nList Active Leases\n")
                leases = self.repo.listActiveLeases()
                for lease in leases:
                    print("-" * 30)
                    print(lease)


            elif choice == "13":
                print("\nList Lease History\n")
                leases = self.repo.listLeaseHistory()
                for lease in leases:
                    print("-" * 30)
                    print(lease)

            elif choice == "14":
                print("\nFind Lease by Lease ID\n")
                
                try:
                    lease_id = int(input("Enter lease ID: "))
                    lease = self.repo.findLeaseById(lease_id)
                    if lease:
                        print("-" * 30)
                        print(lease)
                    else:
                        raise LeaseNotFoundException(f"Lease with ID {lease_id} does not exist.")
                
                except LeaseNotFoundException as Error:
                    print(f"Error in returning a lease based on lease ID {lease_id}: {Error}")


            elif choice == "15":
                print("\nRecord Payment\n")
                
                try:
                    lease_id = int(input("Enter lease ID: "))
                    amount = float(input("Enter payment amount: "))

                    if not self.repo.findLeaseById(lease_id):
                        raise LeaseNotFoundException(f"Lease with ID {lease_id} does not exist.")

                    if amount < 0:
                        raise ValueError("Amount should not be less than zero.")

                    payment = Payment(None, lease_id, amount, date.today())

                    if self.repo.recordPayment(payment, amount):
                        print("Amount added in Payments")
                    else:
                        print("Unable to add payment")

                except LeaseNotFoundException as Error:
                    print(f"Error: {Error}")

                except ValueError as Error:
                    print(f"Invalid input: {Error}")

            elif choice == "16":
                print("\nThank You for Visiting\n")
                print("Exiting system...\n\n")
                break

            else:
                print("Invalid option. Try again.")

if __name__ == "__main__":
    CarRentalSystem().main()
