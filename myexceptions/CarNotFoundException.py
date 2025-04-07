class CarNotFoundException(Exception):
    def __init__(self, message="Car ID not found in the database."):
        super().__init__(message)
