############################
## Logging
############################
##
import logging

## logging settings
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M'
)
logging.debug("This is a debug message")
logging.info("This is an info message") # debug / info / warning / error / critical

## multiple loggers
logger1=logging.getLogger("module1")
logger1.setLevel(logging.DEBUG)
logger2=logging.getLogger("module2")
logger2.setLevel(logging.WARNING)
logger1.debug("This is a debug for module1")
logger2.warning("This is a warning for module2")


