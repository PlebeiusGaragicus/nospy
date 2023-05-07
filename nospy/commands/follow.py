import logging
logger = logging.getLogger("nospy")

from nospy.config import Config


def follow(opts):
    pubkey = opts.get("<pubkey>", None)
    name = opts.get("--name", None)

    if pubkey is None:
        logger.error("Please specify a pubkey to follow.")
        return

    if pubkey in Config.get_instance().following:
        logger.error(f"Already following {pubkey}")
        return

    logger.debug(f"Following... '{pubkey}'")
    Config.get_instance().follow(pubkey, name)
    Config.get_instance().save_config()
