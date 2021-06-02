from __future__ import annotations

import logging


class Subcomponent:
    def do(self):
        result = "subcomponent called"
        logging.debug(result)
        return result
