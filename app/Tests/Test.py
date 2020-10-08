"""
Test file
"""


class Test:
    """
    Test class
    Runs unit tests on project
    """
    def __init__(self):
        self.methods = []
        self.exceptions = []

    def execute_tests(self):
        """
        Execute
        """
        for method in self.methods:
            try:
                method()
            except Exception as e:
                self.exceptions.append(e)
        print(self.exceptions)
        return
