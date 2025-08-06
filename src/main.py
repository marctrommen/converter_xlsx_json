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

supported error codes:
0: Success
1: Invalid class parameters
10: Error reading Excel files:The specified reading folder does not exist
11: Error reading Excel files
20: Error validating data
30: Error exporting to JSON
31: Error removing existing JSON output file
"""

import config
from app import Application
from excel_reader import ExcelReader
from data_validator import DataValidator
from json_writer import JsonWriter

import logging
from logging_config import setup_logging
setup_logging()

logger = logging.getLogger("myapp")


# -----------------------------------------------------------------------------
def main() -> None:
    """This main function initializes the application configuration, 
    sets up logging. It serves as a wrapper for the application.
    
    The principle of IOC (Inversion of Control) is used to inject dependencies
    into the Application class."""

    configuration = config.configuration()
    excel_reader = ExcelReader()
    data_validator = DataValidator()
    json_writer = JsonWriter()

    application = Application(configuration=configuration,
                              excel_reader=excel_reader,
                              data_validator=data_validator,
                              json_writer=json_writer)
    
    exit_code = application.run()
    
    if exit_code == 0:
        logger.info("Application finished successfully.")
    else:
        logger.error("Application finished with exit code: %d", exit_code)
    
    exit(exit_code)
    

# -----------------------------------------------------------------------------
if __name__ == '__main__':
    logger.info("Application started.")
    main()
