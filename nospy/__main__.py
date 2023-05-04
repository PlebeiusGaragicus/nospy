import logging
import docopt

from nospy.config import config, Config
from nospy.logger import setup_logging

# COMMANDS:
from nospy.usage import USAGE
from nospy.version import VERSION
# ...
from nospy.commands.setprivate import set_private_key
from nospy.commands.public import show_public_key
from nospy.commands.key_gen import key_gen


def main():
    setup_logging()
    logger = logging.getLogger("nospy")

    global config
    config = Config()


    args = docopt.docopt(USAGE, version=f"nospy {VERSION}")
    # logger.debug(f"args: {args}")

    passed_args = {k: v for k, v in args.items() if v not in (False, [], None)}
    logger.debug(f"passed args: {passed_args}")

    ### COMMANDS ###
    if args.get("version", False):
        print(f"nospy {VERSION}")

    elif args.get("setprivate", False):
        set_private_key(args)
        config.save_config() #TODO NOT TESTED!!!

    elif args.get("public", False):
        show_public_key(args)

    elif args.get("publish", False):
        print("publishing...")

    elif args.get("follow", False):
        pubkey = args["<pubkey>"]
        print(f"following {pubkey}")

    elif args.get("unfollow", False):
        pubkey = args["<pubkey>"]
        print(f"unfollowing {pubkey}")

    elif args.get("following", False):
        print("showing everyone you follow...")

    elif args.get("key-gen", False):
        key_gen(args)


if __name__ == '__main__':
    main()
