from util.DBConnection import DBConnection
from util.PropertyUtil import PropertyUtil
from dao.ICarLeaseRepository import ICarLeaseRepository
from entity.CarManagement import Vehicle
from entity.CustomerManagement import Customer
from entity.LeaseManagement import Lease
from myexceptions.CarNotFoundException import CarNotFoundException
from myexceptions.CustomerNotFoundException import CustomerNotFoundException
from myexceptions.LeaseNotFoundException import LeaseNotFoundException
from datetime import date

class ICarLeaseRepositoryImpl(ICarLeaseRepository):
    def __init__(self):
        self.connection = DBConnection.getConnection()
        self.cursor = self.connection.cursor()
   

    def addCar(self, car: Vehicle) -> None:
        """
            Function to add Car if not exist
        """
        
        try:
            check_query = "SELECT 1 FROM Vehicle WHERE vehicleID = ?;"
            self.cursor.execute(check_query, (car.get_vehicleID(),))
            if self.cursor.fetchone():
                print(f"\nCar with ID {car.get_vehicleID()} already exists.")
                return False

            query = """
                     INSERT INTO Vehicle(vehicleID, make, model, year, dailyRate, status, passengerCapacity, engineCapacity) 
                     VALUES(?, ?, ?, ?, ?, ?, ?, ?);
                    """
           
            self.cursor.execute(query, (
                car.get_vehicleID(),  
                car.get_make(),  
                car.get_model(),  
                car.get_year(),  
                car.get_dailyRate(),  
                car.get_status(),  
                car.get_passengerCapacity(),  
                car.get_engineCapacity()
            ))
            self.connection.commit()
            return True

        except Exception as Error:
             print(f"Error in adding a car: {Error}")
             return False

    
    def removeCar(self, car_id: int) -> None:
        """
        Function to remove a car after deleting related leases and payments.
        """
        
        try:
            # Check for leases associated with the car
            self.cursor.execute("SELECT leaseID FROM Lease WHERE vehicleID = ?;", (car_id,))
            leases = self.cursor.fetchall()

            for lease in leases:
                lease_id = lease[0]

                # Delete payments linked to each lease
                self.cursor.execute("DELETE FROM Payment WHERE leaseID = ?;", (lease_id,))

                # Delete the lease
                self.cursor.execute("DELETE FROM Lease WHERE leaseID = ?;", (lease_id,))

            # Delete the vehicle
            self.cursor.execute("DELETE FROM Vehicle WHERE vehicleID = ?;", (car_id,))
            self.connection.commit()
            return True

        except Exception as Error:
            print(f"Error in deleting a car: {Error}")
            return False


    
    def listAvailableCars(self) -> list[Vehicle]:
        """
            Function to list all the available Cars
        """

        try:
            query = "SELECT * FROM Vehicle where status = 1;"
                    
           
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            return [Vehicle(*row) for row in rows]
           
        except Exception as Error:
             print(f"Error in displaying all the available cars: {Error}")
             return []
    

    def listRentedCars(self) -> list[Vehicle]:
        """
            Function to list all the rented Cars
        """

        try:
            query = "SELECT * FROM Vehicle WHERE status = 0;"
           
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            return [Vehicle(*row) for row in rows]
           
        except Exception as Error:
             print(f"Error in displaying all the Rented cars: {Error}")
             return []        

    
    def findCarById(self, car_id: int) -> Vehicle:
        """
            Function to find a car
        """

        try:
            query = "SELECT * FROM Vehicle WHERE vehicleID = ?;"
                    
            self.cursor.execute(query, (car_id, ))
            row = self.cursor.fetchone()

            if row:
                return Vehicle(*row)

            raise CarNotFoundException(f"Car with ID {car_id} does not exist.")
            return False

        except CarNotFoundException:
            raise

        except Exception as Error:
            print(f"Error in finding a car: {Error}")
            return None

    def addCustomer(self, customer: Customer) -> None:
        
        """
            Function to add a customer
        """

        try:
            query = """
                        INSERT INTO Customer (customerID, firstName, lastName, email, phoneNumber) 
                        VALUES(?, ?, ?, ?, ?);
                    """
           
            self.cursor.execute(query, (

                customer.get_customerID(),
                customer.get_firstName(),
                customer.get_lastName(),
                customer.get_email(),
                customer.get_phoneNumber()
            ))
            
            self.connection.commit()
            return True
           
        except Exception as Error:
             print(f"Error in adding a customer: {Error}")
             return False     

    
    def removeCustomer(self, customer_id: int) -> bool:
       
        """
            Removes a customer by first deleting related payments, then lease, then customer.
        """
        
        try:
            # Check if lease exists for the customer
            check_lease_query = "SELECT leaseID FROM Lease WHERE customerID = ?;"
            self.cursor.execute(check_lease_query, (customer_id,))
            lease_rows = self.cursor.fetchall()

            for lease_row in lease_rows:
                lease_id = lease_row[0]

                # Delete payments linked to that lease
                delete_payment_query = "DELETE FROM Payment WHERE leaseID = ?;"
                self.cursor.execute(delete_payment_query, (lease_id,))

                # Delete lease linked to customer
                delete_lease_query = "DELETE FROM Lease WHERE leaseID = ?;"
                self.cursor.execute(delete_lease_query, (lease_id,))

            # Delete customer
            delete_customer_query = "DELETE FROM Customer WHERE customerID = ?;"
            self.cursor.execute(delete_customer_query, (customer_id,))

            self.connection.commit()
            return True

        except Exception as Error:
            print(f"Error in deleting customer {customer_id}: {Error}")
            return False

    
    def listCustomers(self) -> list[Customer]:
        """
            Function to list all the customer
        """

        try:
            query = "SELECT * FROM Customer;"
           
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            return [Customer(*row) for row in rows]
           
        except Exception as Error:
             print(f"Error in listing all the customers: {Error}")
             return [] 

    
    def findCustomerById(self, customer_id: int) -> Customer:
        """
            Finding a Customer by customer id
        """

        try:
            query = "SELECT * FROM Customer WHERE customerID = ?;"

            self.cursor.execute(query, (customer_id,))
            row = self.cursor.fetchone()

            if row:
                return Customer(*row)
            
            raise CustomerNotFoundException(f"Customer with ID {customer_id} does not exist.")
            
        except CustomerNotFoundException:
            raise

        except Exception as Error:
            print(f"Unexpected error while finding customer: {Error}")
            return None

    
    def createLease(self, customer_id: int, car_id: int, start_date: date, end_date: date, type: str) -> Lease:
        """
            Inserting a Lease record and returning the Lease object.
        """

        try:
            # Get the next leaseID 
            lease_id_query = "SELECT MAX(leaseID) FROM Lease;"
            self.cursor.execute(lease_id_query)
            result = self.cursor.fetchone()
            lease_id = result[0] + 1 if result and result[0] is not None else 1

            insert_query = """
                           INSERT INTO Lease (leaseID, vehicleID, customerID, startDate, endDate, type) 
                           VALUES (?, ?, ?, ?, ?, ?);
                           """
            self.cursor.execute(insert_query, (

                lease_id, car_id, 
                customer_id, 
                start_date.strftime("%Y-%m-%d"), 
                end_date.strftime("%Y-%m-%d"), 
                type
                ))

            updateStatusQuery = """
                                UPDATE Vehicle SET status = 0 
                                WHERE vehicleID = ?
                                """
            self.cursor.execute(updateStatusQuery, (car_id, ))
            self.connection.commit()
            return Lease(lease_id, car_id, customer_id, start_date, end_date, type)

        except Exception as Error:
            print(f"Error in inserting a lease record: {Error}")
            return False


    def returnCar(self, lease_id: int) -> Lease:
        """
            Returning a car details and lease details by lease_id
        """

        try:
            query = """
                SELECT v.vehicleID, v.make, v.model, v.year, l.customerID, l.startDate, l.endDate, l.type
                FROM Vehicle v
                JOIN Lease l ON
                v.vehicleID = l.vehicleID
                WHERE l.leaseID = ?;
                """

            self.cursor.execute(query, (lease_id,))
            row = self.cursor.fetchone()

            if row:
                lease = Lease(leaseID=lease_id, vehicleID=row[0], customerID=row[4], startDate=row[5], endDate=row[6], type=row[7])
                vehicle_details = {
                "make": row[1],
                "model": row[2],
                "year": row[3]
            }
                return lease, vehicle_details
            return None, None

        except Exception as Error:
            print(f"Error in returning a  car based on lease ID {lease_id}: {Error}")
            return None

    
    def listActiveLeases(self) -> list[Lease]:
        """
            Returns a list of active lease records based on current date.
        """
    
        try:
            today = date.today().strftime("%Y-%m-%d")
            query = "SELECT * FROM Lease WHERE startDate <= ? AND endDate >= ?;"

            self.cursor.execute(query, (today, today))
            rows = self.cursor.fetchall()
            return [Lease(*row) for row in rows]

        except Exception as Error:
            print(f"Error in retrieving active leases: {Error}")
            return []

    
    def listLeaseHistory(self) -> list[Lease]:
        """
            Returns a list of all lease records
        """
    
        try:
            query = "SELECT * FROM Lease ORDER BY startDate"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            return [Lease(*row) for row in rows]

        except Exception as Error:
            print(f"Error in retrieving lease history: {Error}")
            return []


    def findLeaseById(self, lease_id: int) -> Lease:
        """
            Returning lease details based on lease id
        """

        try:
            self.cursor.execute("SELECT * FROM Lease WHERE leaseID = ?;", (lease_id,))
            result = self.cursor.fetchone()
            
            if result:
                return Lease(*result)
        
            raise LeaseNotFoundException(f"Lease with ID {lease_id} does not exist.")
        
        except LeaseNotFoundException:
            raise

        except Exception as Error:
            print(f"Unexpected error while finding Lease: {Error}")
            return None            

    def recordPayment(self, lease: Lease, amount: float) -> None:
        """
            Insert a record for payment after verifying the lease exists.
        """
        
        try:

            lease_obj = self.findLeaseById(lease.get_leaseID())
            if not lease_obj:
                return False

            # Get the next paymentID
            self.cursor.execute("SELECT MAX(paymentID) FROM Payment;")
            result = self.cursor.fetchone()
            payment_id = result[0] + 1 if result and result[0] is not None else 1

            payment_date = date.today().strftime("%Y-%m-%d")

            insert_query = """
                           INSERT INTO Payment (paymentID, leaseID, amount, paymentDate)
                           VALUES (?, ?, ?, ?)
                           """
            self.cursor.execute(insert_query, (payment_id, lease.get_leaseID(), amount, payment_date))
            self.connection.commit()
            return True

        except Exception as Error:
            print(f"Error in recording payment: {Error}")
            return False

    def closeConnection(self):
        try:
            if self.cursor:
                self.cursor.close()

            if self.connection:
                self.connection.close()
            print("Database connection closed successfully.\n\n")

        except Exception as Error:
            print(f"Error while closing database connection: {Error}")


