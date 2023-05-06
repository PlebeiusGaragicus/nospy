import sys
import os
import logging

import docopt

# from nospy.config import config, Config
from nospy.config import config
# from nospy.config import init_config
from nospy.logger import setup_logging


# COMMANDS:
from nospy.usage import USAGE
from nospy.version import VERSION
# ...
from nospy.commands.setprivate import set_private_key
from nospy.commands.public import show_public_key
from nospy.commands.key_gen import key_gen


def main():
    if os.getenv("DEBUG", False):
        print("-"*100)

    setup_logging()
    logger = logging.getLogger("nospy")

    # global config
    # config = Config()


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
        priv = set_private_key(args)
        if not priv:
            sys.exit(1)
        logger.info(f"hex private key: {priv}")

        config.private_key = priv
        config.save_config()

        logger.info("Private key set successfully.")

    ### PUBLIC ##########################
    elif args.get("public", False):
        show_public_key(args)

    ### PUBLISH #########################
    elif args.get("publish", False):
        print("publishing...")

    ### FOLLOW ##########################
    elif args.get("follow", False):
        pubkey = args["<pubkey>"]
        print(f"following {pubkey}")

    ### UNFOLLOW ########################
    elif args.get("unfollow", False):
        pubkey = args["<pubkey>"]
        print(f"unfollowing {pubkey}")

    ### FOLLOWING #######################
    elif args.get("following", False):
        print("showing everyone you follow...")

    ### KEY-GEN #########################
    elif args.get("key-gen", False):
        key_gen(args)
