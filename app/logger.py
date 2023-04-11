import logging
from app import configuration

logging.getLogger('werkzeug').setLevel(logging.ERROR)
logging.getLogger('googleapicliet.discovery_cache').setLevel(logging.ERROR)

def setup_custom_logger(name):
    formatter = logging.Formatter(
        fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s')

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(configuration.LOG_LEVEL)
    logger.addHandler(handler)

    return logger
