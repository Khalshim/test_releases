import unittest

from white_app_python.my_class import MyClass


class MyClassTest(unittest.TestCase):
    def setUp(self):
        self.my_class = MyClass()

    def tearDown(self):
        # To be implemented if required
        pass

    def test_something(self):
        result = self.my_class.do()
        self.assertEqual(result, "MyClass call to subcomponent : subcomponent called")
