"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Created by seroneymatoke
Date: 22.11.21
Purpose: Implement Logger Functions for test data
Implementation: Appends all logged info to automation.log
TestData: None
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import inspect
import logging


class CustomLogger:

    @staticmethod
    def custom_logger(log_level=logging.DEBUG):
        # set class/module method from where function is called
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(log_level)
        file_handler = logging.FileHandler("automation.log")
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s: - %(message)s', datefmt='%m/%d/%Y %I:%M:%S%p')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger
