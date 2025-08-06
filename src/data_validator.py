#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger("myapp.DataValidator")


# -----------------------------------------------------------------------------
class DataValidator:
    """This class is responsible for validating the data extracted from Excel files."""

    # -----------------------------------------------------------------------------
    def __init__(self) -> None:
        """Initialize the DataValidator."""
        logger.debug("DataValidator initialized")        

        self.error_code = 0


    # -----------------------------------------------------------------------------
    def validate_data(self, data: dict) -> int:
        """Validate the data extracted from Excel files.
        Returns 0 if validation is successful, otherwise returns an error code."""
        logger.debug("Validating data")

        self.error_code = 0

        if ((data is None) or (not isinstance(data, dict))):
            logger.error("Invalid data format: expected a dictionary")
            self.error_code = 20
    
        # iterate through the data to check for required fields
        for worksheet_id, worksheet_data in data.items():
            logger.debug("Validating worksheet: %s", worksheet_id)
            
            if self.error_code == 0:
                self._validate_worksheet_data(worksheet_id, worksheet_data)
            
        return self.error_code
    

    # -----------------------------------------------------------------------------
    def _validate_worksheet_data(self, worksheet_id: str, worksheet_data: dict) -> None:
        """Validate the data structure of a single worksheet.
        This method can be extended to implement specific validation rules.
        For example, check for required fields, data types, etc."""
        logger.debug("Validating worksheet data for: %s", worksheet_id)

        if not worksheet_data:
            logger.error("Worksheet data is empty")
            self.error_code = 20
        
        if self.error_code == 0:
            data_count = len(worksheet_data.keys())
            if data_count == 17:
                logger.debug("Worksheet data for '%s' is valid", worksheet_id)
            else:
                logger.error("Worksheet '%s' has an invalid number of fields: %d", worksheet_id, data_count)
                self.error_code = 20
        