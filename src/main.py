#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Main entry point for the converter-xlsx-json application.
This script initializes the application, sets up logging, and runs the main function.

This application reads all .xlsx files in a directory, processes only worksheets 
starting with SST_, and stores their content in an internal data structure. 

After optional data validations with error logging, the validated data is exported 
as a structured JSON file.

Internal error handling is done via exit codes, which can be used by other
applications to determine the success (exit code 0) or failure (exit code <> 0)
of the conversion process.
"""

import config

import logging
from logging_config import setup_logging
setup_logging()

logger = logging.getLogger("myapp")


# -----------------------------------------------------------------------------
def main() -> None:
    """This main function initializes the application configuration, 
    sets up logging. It serves as the entry point for the application.
    
    Application setup follows the IOC (Inversion of Control) principle."""
    configuration = config.configuration()


# -----------------------------------------------------------------------------
if __name__ == '__main__':
    logger.info("Application started.")
    main()
    logger.info("Application finished")
    exit(0)
