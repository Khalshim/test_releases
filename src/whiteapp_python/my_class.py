import logging

from .component.component import Component


class MyClass:
    def __init__(self):
        self.att1 = "attribut"

    def do(self):
        component = Component()
        my_string = f"MyClass attribute : {self.att1}"
        logging.debug(my_string)
        my_string = f"MyClass call to component : {component.do()}"
        logging.debug(my_string)
        return my_string
