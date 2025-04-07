class CustomerNotFoundException(Exception):
    def __init__(self, message="Customer ID not found in the database."):
        super().__init__(message)
