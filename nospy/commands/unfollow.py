import logging
logger = logging.getLogger("nospy")

from nospy.config import Config


def unfollow(args):
    pubkey = args.get('<pubkey>', None)

    # shouldn't need this because of docopt
    # if pubkey is None:
    #     logger.error("Please specify a pubkey to unfollow.")
    #     return

    if pubkey:
        removed = Config.get_instance().unfollow(pubkey)
        if removed:
            # logger.info(f"No longer following: {pubkey}")
            print(f"No longer following: {pubkey}")
            Config.get_instance().save_config()
        else:
            logger.error(f"You're not following: {pubkey}")
