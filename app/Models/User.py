"""

"""

from .Model import Model


class User(Model):
    """

    """
    def __init__(self):
        super().__init__()
        self.table = 'users'
        self.attributes = [
            'id',
            'first_name',
            'last_name',
            'role',
            'email_address',
            'password',
        ]
