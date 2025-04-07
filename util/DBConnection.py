import pyodbc
import sys
from util.PropertyUtil import PropertyUtil

sys.path.append(r"F:/Hexaware Training/Python/CarRentalSystem")

class DBConnection:
    connection = PropertyUtil.getPropertyString()

    @staticmethod
    def getConnection():
        try:
            return pyodbc.connect(DBConnection.connection)
        except Exception as e:
            print("Error connecting to the database:", e)
            return None

            