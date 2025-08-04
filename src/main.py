#!/usr/bin/env python
# -*- coding: utf-8 -*-


import config

import logging
from logging_config import setup_logging
setup_logging()

logger = logging.getLogger("myapp")


# -----------------------------------------------------------------------------
def main() -> None:
    """Main function to run the application.
    """
    configuration = config.configuration()
    print("Hello from converter-xlsx-json!")


# -----------------------------------------------------------------------------
if __name__ == '__main__':
    logger.info("Application started.")
    main()
    logger.info("Application finished")
    exit(0)
