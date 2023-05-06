import sys
import os
import logging

import docopt

from nospy.config import Config
from nospy.logger import setup_logging


# COMMANDS:
from nospy.usage import USAGE
from nospy.version import VERSION
# ...
from nospy.commands.setprivate import set_private_key
from nospy.commands.public import show_public_key
from nospy.commands.private import show_private_key
from nospy.commands.key_gen import key_gen
from nospy.commands.relay_add import relay_add
from nospy.commands.relay_remove import relay_remove


def main():
    if os.getenv("DEBUG", False):
        print("-"*100)

    setup_logging()
    logger = logging.getLogger("nospy")


    args = docopt.docopt(USAGE, version=f"nospy {VERSION}")
    # logger.debug(f"args: {args}")

    passed_args = {k: v for k, v in args.items() if v not in (False, [], None)}
    logger.debug(f"passed args: {passed_args}")

    #####################################
    ### COMMANDS ########################
    #####################################


    ### VERSION #########################
    if args.get("version", False):
        print(f"nospy {VERSION}")

    ### SETPRIVATE ######################
    elif args.get("setprivate", False):
        set_private_key(args)
        # priv = set_private_key(args)
        # if not priv:
        #     sys.exit(1)
        # logger.info(f"hex private key: {priv}")

        # Config.get_instance().private_key = priv
        # Config.get_instance().save_config()
        # logger.info("Private key set successfully.")

    ### PUBLIC ##########################
    elif args.get("public", False):
        show_public_key(args)

    ### PRIVATE ##########################
    elif args.get("private", False):
        show_private_key(args)

    ### PUBLISH #########################
    elif args.get("publish", False):
        logger.info("publishing...")

    ### FOLLOW ##########################
    elif args.get("follow", False):
        pubkey = args["<pubkey>"]
        logger.info(f"following {pubkey}")

    ### UNFOLLOW ########################
    elif args.get("unfollow", False):
        pubkey = args["<pubkey>"]
        logger.info(f"unfollowing {pubkey}")

    ### FOLLOWING #######################
    elif args.get("following", False):
        logger.info("showing everyone you follow...")

    ### KEY-GEN #########################
    elif args.get("key-gen", False):
        key_gen(args)

    ### RELAY-ADD #######################
    elif args.get("relay-add", False):
        relay_add(args)

    ### RELAY-REMOVE #######################
    elif args.get("relay-remove", False):
        relay_remove(args)
