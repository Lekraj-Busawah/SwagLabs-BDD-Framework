import logging

class LogGen:
    @staticmethod
    def loggen():
        # This sets up a log file named automation.log
        logging.basicConfig(filename="automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger