class LeaseNotFoundException(Exception):
    def __init__(self, message="Lease ID not found in the database."):
        super().__init__(message)
