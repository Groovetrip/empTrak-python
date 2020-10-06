"""

"""

from .Model import Model


class Employee(Model):
    """

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
