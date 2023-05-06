import logging
logger = logging.getLogger("nospy")

from nospy.config import Config


def unfollow(pubkey):
    # pubkey = opts.get('<pubkey>', None)

    if pubkey:
        removed = Config.get_instance().unfollow(pubkey)
        if removed:
            logger.info(f"No longer following {pubkey}.")
            Config.get_instance().save_config()
        else:
            logger.error(f"You're not following: {pubkey}")
