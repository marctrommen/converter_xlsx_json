#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Configuration module for the application.
This module contains the global configuration for the application.
It sets up the project directories, files and other constants.
It also initializes the logging and locale settings.
This configuration is used throughout the application to ensure consistent settings."""

import os
import datetime
import locale

import logging
logger = logging.getLogger("myapp.configuration")

# -----------------------------------------------------------------------------
def configuration() -> dict:
    """Global configuration of the application.
    The configuration is stored in a dictionary which is returned by the function.
    It contains various settings such as project directories, file paths, 
    and other constants."""

    logger.debug("global configuration started")
    config = {}
    locale.setlocale(locale.LC_ALL, '')
    config['GENERATOR_STARTED'] = datetime.datetime.now()
    config['CURRENT_YEAR'] = config['GENERATOR_STARTED'].strftime('%Y')
    config['GENERATED_DATETIME'] = config['GENERATOR_STARTED'].strftime('%Y%m%d %H%M%S')
    config['GENERATED_DATETIME_HUMAN_READABLE'] = config['GENERATOR_STARTED'].strftime('%d.%m.%Y %H:%M:%S')

    aPath = os.path.realpath(__file__)
    aPath = os.path.dirname(aPath)
    aPath = os.path.normpath(aPath)
    aPath = os.path.join(aPath, "..")
    aPath = os.path.normpath(aPath)
    config["PROJECT_ROOT_DIR"] = aPath
    config["SRC_DIR"] = os.path.join( config["PROJECT_ROOT_DIR"], "src" )
    config["DATA_DIR"] = os.path.join( config["PROJECT_ROOT_DIR"], "data" )

    logger.debug("global configuration done")
    return config

# -----------------------------------------------------------------------------
if __name__ == '__main__':
    raise RuntimeError("This is a configuration module and should not get run directly")