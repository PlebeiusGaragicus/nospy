import os
import logging

import docopt

from nospy.logger import setup_logging


from nospy.usage import USAGE
from nospy.version import VERSION

from nospy.commands.setprivate import set_private_key
from nospy.commands.public import show_public_key
from nospy.commands.private import show_private_key
from nospy.commands.publish import publish
from nospy.commands.follow import follow
from nospy.commands.unfollow import unfollow
from nospy.commands.following import following
from nospy.commands.home import home
from nospy.commands.getinfo import get_info
from nospy.commands.keygen import key_gen
from nospy.commands.relay_add import relay_add
from nospy.commands.relay_remove import relay_remove
from nospy.commands.relays import relays
from nospy.commands.users import users
from nospy.commands.upload import upload


def main():
    if os.getenv("DEBUG", False):
        print("-"*100)

    setup_logging()
    logger = logging.getLogger("nospy")

    args = docopt.docopt(USAGE, version=f"nospy {VERSION}")

    passed_args = {k: v for k, v in args.items() if v not in (False, [], None)}
    logger.debug(f"passed args: {passed_args}")

    #####################################
    ### COMMANDS ########################
    #####################################
    if args.get("version", False):
        print(f"nospy {VERSION}")
    elif args.get("setprivate", False):
        set_private_key(args)
    elif args.get("public", False):
        show_public_key(args)
    elif args.get("private", False):
        show_private_key(args)
    elif args.get("publish", False):
        publish(args)
    elif args.get("follow", False):
        follow(args)
    elif args.get("unfollow", False):
        unfollow(args)
    elif args.get("following", False):
        following(args)
    elif args.get("getinfo", False):
        get_info(args)
    elif args.get("home", False):
        home(args)
    elif args.get("keygen", False):
        key_gen(args)
    elif args.get("relay-add", False):
        relay_add(args)
    elif args.get("relay-remove", False):
        relay_remove(args)
    elif args.get("relays", False):
        relays(args)
    elif args.get("users", False):
        users()
    elif args.get("upload", False):
        upload(args)
