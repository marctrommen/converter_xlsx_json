#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from excel_reader import ExcelReader
import json

import logging
logger = logging.getLogger("myapp.Application")


# -----------------------------------------------------------------------------
class Application:
    """This class is responsible for managing the application lifecycle and coordinating"""


    # -----------------------------------------------------------------------------
    def __init__(self, 
                 configuration: dict,
                 excel_reader: ExcelReader) -> None:
        """Initialize the Application with the given configuration."""

        self.exit_code = 0

        if ((configuration is None) or (not isinstance(configuration, dict)) or
            (excel_reader is None) or (not isinstance(excel_reader, ExcelReader))):
            self.exit_code = 1
            logger.error("Invalid configuration or ExcelReader instance")

        self.data = {}
        if self.exit_code == 0:
            self.data["CONFIG"] = configuration
            self.excel_reader = excel_reader

        logger.debug("Application initialized with configuration")
    

    # -----------------------------------------------------------------------------
    def run(self) -> int:
        """Run the main application logic."""

        logger.debug("Running application")
        
        # Initialize data structures
        self.data["INTERIM_DATA"] = {}
        self.data["EXCEL_DATA"] = {}

        if self.exit_code == 0:
            self._clean_up()

        if self.exit_code == 0:
            self._get_all_files_from_folder(
                self.data["CONFIG"]["DATA_DIR"], 
                self.data["CONFIG"]["FILE_EXTENSION_XLSX"]
            )
        
        if self.exit_code == 0:
            self._read_excel_files()
        
        if self.exit_code == 0:
            self._validate_data()

        if self.exit_code == 0:
            self._export_to_json()
        
        return self.exit_code


    # -----------------------------------------------------------------------------
    def _clean_up(self) -> None:
        """Delete JSON result file if any exists before starting a new ."""

        logger.debug("Cleaning up resources")

        aPath = self.data["CONFIG"]["JSON_OUTPUT_FILE"]
        if os.path.isfile(aPath):
            try:
                os.remove(aPath)
                logger.debug("Removed existing JSON output file: %s", aPath)
            except OSError as error:
                logger.error("Error removing existing JSON output file: %s", error)
                self.exit_code = 31


    # -----------------------------------------------------------------------------
    def _get_all_files_from_folder(self, directory: str, file_extension: str) -> None:
        """Get all files from the specified directory, filter them by file_extension for
        Excel files and store the result into data structure 
        data["INTERIM_DATA"]["EXCEL_FILE_LIST"]."""
        
        logger.debug("Getting all files from folder")

        file_list = []
        
        if os.path.isdir(directory):
            files = os.listdir(directory)
            for file in files:
                if file.endswith(file_extension):
                    filename = os.path.join(directory, file)
                    if os.path.isfile(filename):
                        file_list.append(filename)
                        logger.debug("Excel file found: %s", filename)
            if len(file_list) == 0:
                logger.warning("No Excel files found in directory: %s", directory)
        else:
            logger.error("The specified directory for reading Excel files does not exist: %s", directory)
            self.exit_code = 10

        self.data["INTERIM_DATA"]["EXCEL_FILE_LIST"] = file_list

    # -----------------------------------------------------------------------------
    def _read_excel_files(self) -> None:
        """Read all Excel files from file list, extract data from worksheets 
        with the help of class ExcelReader and store the data in"""

        logger.debug("Reading Excel files")

        for file_path in self.data["INTERIM_DATA"]["EXCEL_FILE_LIST"]:
            logger.debug("Reading Excel file: %s", file_path)

            if self.exit_code == 0:
                self.excel_reader.read_excel_file(
                    excel_file_path=file_path,
                    worksheet_prefix=self.data["CONFIG"]["WORKSHEET_PREFIX"],
                    excel_data=self.data["EXCEL_DATA"]
                )

    # -----------------------------------------------------------------------------
    def _validate_data(self) -> None:
        """Validate the data read from Excel files.
        This method should implement the validation logic and set self.exit_code accordingly."""
        logger.debug("Validating data")

        # If validation fails, set self.exit_code to 20
        if not self.data["EXCEL_DATA"]:
            logger.error("No data found in Excel files")
            self.exit_code = 20
            return
        
        for worksheet_id, worksheet_data in self.data["EXCEL_DATA"].items():
            logger.debug("Validating worksheet: %s", worksheet_id)

            if not worksheet_data:
                logger.error("Worksheet '%s' is empty", worksheet_id)
                self.exit_code = 20
                return
            
    # -----------------------------------------------------------------------------
    def _export_to_json(self) -> None:
        """Export the validated data to a JSON file.
        This method should implement the export logic and set self.exit_code accordingly."""
        logger.debug("Exporting data to JSON")

        # Serializing json
        json_data = json.dumps(self.data["EXCEL_DATA"], indent=4, ensure_ascii=False)
        print(json_data)
        
        file_name = self.data["CONFIG"]["JSON_OUTPUT_FILE"]
        with open(file_name, "w", encoding="utf-8") as outfile:
            outfile.write(json_data)
