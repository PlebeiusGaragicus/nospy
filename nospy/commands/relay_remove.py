import logging
logger = logging.getLogger("nospy")

from nospy.config import Config


def relay_remove(opts):
    addr = opts.get('<url>', None)
    all_relays = opts.get('--all', False)

    if not addr and not all_relays:
        logger.error("Please specify a relay address or use --all.")
        return


    if addr:
        removed = Config.get_instance().remove_relay(addr)
        if removed:
            logger.info(f"Removed relay {addr}.")
            Config.get_instance().save_config()
        else:
            # logger.error(f"Relay {addr} not found. You're not subscribed to this relay.")
            logger.error(f"You're not subscribed to relay: {addr}")

    if all_relays:
        Config.get_instance().clear_relays()
        Config.get_instance().save_config()
        logger.info("Removed all relays.")
