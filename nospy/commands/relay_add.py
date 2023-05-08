import logging
logger = logging.getLogger("nospy")

from nospy.config import Config


def relay_add(opts):
    addr = opts['<url>']

    if not addr:
        logger.error("Please specify a relay address.")
        return

    if addr in Config.get_instance().relays:
        logger.warn(f"Relay '{addr}' has already been added.")
        return

    logger.info(f"Adding relay: {addr}")
    Config.get_instance().add_relay(addr, {
        'read': True,
        'write': True,
    })

    Config.get_instance().save_config()
    # logger.debug(f"Relay added: {addr}")
