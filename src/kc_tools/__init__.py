import logging

logger = logging.getLogger('kc_tools')
logger.setLevel(logging.ERROR)  # Set the log level to ERROR

file_handler = logging.FileHandler('error.log')
file_handler.setLevel(logging.ERROR)  # Set the log level for the handler

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
