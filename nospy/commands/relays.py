import logging
logger = logging.getLogger("nospy")

from nospy.config import Config

def relays(opts):

    relays = Config.get_instance().relays

    if relays == {}:
        logger.info("No relays saved.")
        return

    logger.info("Listing all relays:")

    for n, relay in enumerate(relays):
        print(f"{n+1}: {relay}")
