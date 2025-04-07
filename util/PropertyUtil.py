import pyodbc

DRIVER_NAME= "SQL Server"
SERVER = "LAPTOP-2Q84MA0J\SQLEXPRESS"
DATABASE = "CarRentalSystem"
USERNAME = ""
PASSWORD = ""
    
class PropertyUtil:
    @staticmethod
    def getPropertyString():
        connectionString = (
            f"Driver={DRIVER_NAME};"
            f"Server={SERVER};"
            f"Database={DATABASE};"
            f"UID={USERNAME};"
            f"PWD={PASSWORD};")

        return connectionString