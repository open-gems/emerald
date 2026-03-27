import logging
import sys

class CustomFormatter(logging.Formatter):
    """Custom formatter to add ANSI colors to logs based on level"""
    # ANSI escape codes for colors
    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    green = "\x1b[32;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    
    def __init__(self, fmt: str):
        super().__init__()
        self.fmt = fmt
        self.FORMATS = {
            logging.DEBUG: self.yellow + self.fmt + self.reset,
            logging.INFO: self.green + self.fmt + self.reset,
            logging.WARNING: self.yellow + self.fmt + self.reset,
            logging.ERROR: self.red + self.fmt + self.reset,
            logging.CRITICAL: self.bold_red + self.fmt + self.reset
        }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

def setup_logger(name: str = "app", env: str = 'dev'):
    # Determine level
    log_level = logging.DEBUG if env == "dev" else logging.INFO
    
    # Base format string
    log_format = "%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s"

    # Create handler
    console_handler = logging.StreamHandler(sys.stdout)
    
    # Apply color formatter ONLY if we are in dev
    if env == "dev":
        console_handler.setFormatter(CustomFormatter(log_format))
    else:
        console_handler.setFormatter(logging.Formatter(log_format))

    # Basic config with our custom handler
    logging.basicConfig(
        level=log_level,
        handlers=[console_handler],
        force=True 
    )

    return logging.getLogger(name)