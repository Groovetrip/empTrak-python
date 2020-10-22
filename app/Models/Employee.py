"""
Employee Model file
"""

from Model import Model


class Employee(Model):
    """
    Employee Model class
    Connects to employees table data
    """
    def __init__(self):
        super().__init__()
        self.table = 'employees'
        self.attributes = [
            'id',
            'first_name',
            'last_name',
            'address',
        ]
