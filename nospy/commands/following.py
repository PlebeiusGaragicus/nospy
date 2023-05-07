import logging
logger = logging.getLogger("nospy")

from nospy.config import Config


def following(args):
    following = Config.get_instance().following

    if following == {}:
        logger.info("Not following anyone.  Get some friends!")
        return

    # for f in Config.get_instance().following.items():
    for pubkey, info in Config.get_instance().following.items():
        print(f"{info.get('name', '')}: {pubkey}")
