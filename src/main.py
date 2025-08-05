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
from app import Application

import logging
from logging_config import setup_logging
setup_logging()

logger = logging.getLogger("myapp")


# -----------------------------------------------------------------------------
def main() -> None:
    """This main function initializes the application configuration, 
    sets up logging. It serves as a wrapper for the application."""

    configuration = config.configuration()
    application = Application(configuration)
    exit_code = application.run()
    logger.info("Application finished with exit code: %d", exit_code)
    exit(exit_code)
    

# -----------------------------------------------------------------------------
if __name__ == '__main__':
    logger.info("Application started.")
    main()
