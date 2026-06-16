import logging
import os

LOG_DIR = os.path.join(
    os.getcwd(),
    "logs"
)

os.makedirs(
    LOG_DIR,
    exist_ok=True
)

logger = logging.getLogger(
    "email-threat-intelligence"
)

logger.setLevel(
    logging.INFO
)

logger.propagate = False

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

file_handler = logging.FileHandler(
    os.path.join(
        LOG_DIR,
        "app.log"
    )
)

file_handler.setFormatter(
    formatter
)

console_handler = logging.StreamHandler()

console_handler.setFormatter(
    formatter
)

if not logger.handlers:

    logger.addHandler(
        file_handler
    )

    logger.addHandler(
        console_handler
    )