"""

"""


class Model:
    """

    """
    def __init__(self):
        self.table = None
        self.attributes = []

    @classmethod
    def all(cls):
        """
        Select and return array of all model instances
        :rtype: list
        """
        pass

    @classmethod
    def find(cls, identifier: int):
        """
        Find and return model entry
        :param int identifier:
        :rtype: Model|None
        """
        pass

    @classmethod
    def create(cls, data: dict):
        """
        Store model data and return new instance
        :param dict data:
        :rtype: Model
        """
        pass

    def update(self, data: dict):
        """
        Update instance of model in database
        :param dict data:
        :rtype: Model
        """

        # TODO: Decide if this should be save(), and have an update() class method

        return self

    def delete(self):
        """
        Delete instance of model from database
        """
        return
