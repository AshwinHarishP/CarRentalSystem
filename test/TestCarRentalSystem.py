import unittest
import sys

sys.path.append(r"F:\Hexaware Training\Python\CarRentalSystem")
from dao.ICarLeaseRepositoryImpl import ICarLeaseRepositoryImpl
from entity.CarManagement import Vehicle
from entity.LeaseManagement import Lease
from myexceptions.CustomerNotFoundException import CustomerNotFoundException
from myexceptions.CarNotFoundException import CarNotFoundException
from myexceptions.LeaseNotFoundException import LeaseNotFoundException
from datetime import date


class TestCarRentalSystem(unittest.TestCase):
    def setUp(self):
        self.repo = ICarLeaseRepositoryImpl()
    

    def testCreateCar(self):
        """
            Test case to test car created successfully or not
        """

        carObj = Vehicle(128, "Tesla", "X", "2015-07-12", 5000, 1, 4, 1)
        result = self.repo.addCar(carObj)
        self.assertTrue(result)


    def testCreateLease(self):
        """
            Test case to test lease is created successfully or not
        """

        result = self.repo.createLease(101, 10, date.fromisoformat("2025-01-01"), date.fromisoformat("2025-02-02"), "DailyLease")
        self.assertIsInstance(result, Lease)


    def testRetrievedLease(self):
        """
            Test case to test lease is retrieved successfully or not.
        """

        result = self.repo.listLeaseHistory()
        self.assertGreater(len(result), 0)


    def testIDNotFound(self):
        """
            Test case to test exception is thrown correctly or not when customer id or car id or 
            lease id not found in database
        """

        with self.assertRaises(CustomerNotFoundException):
            self.repo.findCustomerById(-1)

        with self.assertRaises(CarNotFoundException):
            self.repo.findCarById(-1)

        with self.assertRaises(LeaseNotFoundException):
            self.repo.findLeaseById(-1)


if __name__ == '__main__':
    unittest.main()
