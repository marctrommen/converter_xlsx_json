#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger("myapp.ExcelReader")


# -----------------------------------------------------------------------------
class ExcelReader:
    """This class is responsible for reading Excel files (.xlsx) and extracting data
    from worksheets that start with 'SST_'."""

    def __init__(self, 
                 configuration: dict) -> None:
        """Initialize the ExcelReader with the given configuration."""
        self.data = {}
        self.data["CONFIG"] = configuration
        logger.debug("ExcelReader initialized with configuration: %s", self.configuration)

    def read_excel_files(self) -> None:
        """Read all .xlsx files in the specified directory and extract data from 
        worksheets starting with 'SST_'."""
        