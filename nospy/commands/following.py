import logging
logger = logging.getLogger("nospy")

from nospy.config import Config


def following(args):
    # pubkey = opts['<pubkey>']

    following = Config.get_instance().following

    if following == []:
        logger.info("Not following anyone.  Get some friends!")
        return

    for f in Config.get_instance().following:
        print(f"{f}")
