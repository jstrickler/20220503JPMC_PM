import logging
from functools import wraps

logging.basicConfig(
    filename='jpmcdemo.log',
    level = logging.DEBUG,
    format="%(name)s %(levelname)s %(message)s %(asctime)s",
)

def log_calls(original_function):

    @wraps(original_function)
    def replacement_function(*args, **kwargs):
        logging.debug(f"Calling {original_function.__name__}")
        result = original_function(*args, **kwargs)
        return result

    return replacement_function



