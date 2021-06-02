from __future__ import annotations

import logging

from .component.subcomponent import Subcomponent


class MyClass:
    def __init__(self):
        self.att1 = "attribut"

    def do(self):
        subcomponent = Subcomponent()
        my_string = "MyClass call to subcomponent : {}".format(subcomponent.do())
        logging.debug(my_string)
        return my_string
