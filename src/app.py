#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger("myapp.Application")


# -----------------------------------------------------------------------------
class Application:
    """This class is responsible for managing the application lifecycle and coordinating"""

    def __init__(self, 
                 configuration: dict) -> None:
        """Initialize the Application with the given configuration."""

        self.exit_code = 0
        self.data = {}
        self.data["CONFIG"] = configuration
        logger.debug("Application initialized with configuration")
    
    def run(self) -> int:
        """Run the main application logic."""
        logger.info("Running application with configuration: %s", self.data["CONFIG"])
        # Here you would typically call methods to read Excel files, validate data, etc.
        # For example:
        # excel_reader = ExcelReader(self.data["CONFIG"])
        # excel_reader.read_excel_files()
        # self.validate_data()
        # self.export_to_json()
        return self.exit_code
