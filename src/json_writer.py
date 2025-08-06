#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

import logging
logger = logging.getLogger("myapp.JsonWriter")


# -----------------------------------------------------------------------------
class JsonWriter:
    """This class is responsible for writing data to a JSON file."""

    # -----------------------------------------------------------------------------
    def __init__(self) -> None:
        """Initialize the DataValidator."""
        logger.debug("DataValidator initialized")        

        self.error_code = 0


    # -----------------------------------------------------------------------------
    def persist_data(self, file_path: str, data: dict) -> int:
        """Persist the validated data, e.g. to a JSON file.
        This method should implement the export logic and set self.error_code accordingly.
        Returns 0 on success, otherwise returns an error code."""
        logger.debug("Persisting data to JSON file")

        self.error_code = 0

        if ((data is None) or (not isinstance(data, dict))):
            logger.error("Invalid data format: expected a dictionary")
            self.error_code = 30
        
        if self.error_code == 0:
            # Serializing json
            try:
                json_data = json.dumps(data, indent=4, ensure_ascii=False)
            except Exception as e:
                logger.error("Error serializing data to JSON: %s", e)
                self.error_code = 30
        
        if self.error_code == 0:
            try:
                file_name = file_path
                with open(file_name, "w", encoding="utf-8") as outfile:
                    outfile.write(json_data)
            except Exception as e:
                logger.error("Error writing JSON file '%s': %s", file_name, e)
                self.error_code = 31

        return self.error_code
