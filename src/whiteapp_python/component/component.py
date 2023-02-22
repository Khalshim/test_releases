import logging


class Component:
    def do(self) -> str:
        result = "component called"
        logging.debug(result)
        return result
