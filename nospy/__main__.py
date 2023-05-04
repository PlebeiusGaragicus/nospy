import os
import logging
from pathlib import Path
import docopt

# from nospy import VERSION
from nospy.config import config, Config
from nospy.logger import setup_logging

# COMMANDS:
from nospy.commands.home import home
# ...
from nospy.commands.setprivate import set_private_key
from nospy.commands.public import show_public_key
from nospy.commands.key_gen import key_gen

VERSION = '0.0.1'

# NOTE: This usage string is very important.  Since we are using docopt, it is used to parse the command line arguments.
USAGE = '''
noscl

Usage:
  noscl home [--verbose] [--json] [--onlyreplies] [--noreplies] [--kinds=<kinds>...] [--since=<since>] [--until=<until>] [--limit=<limit>]
  noscl inbox [--verbose] [--json] [--onlyreplies] [--noreplies] [--since=<since>] [--until=<until>] [--limit=<limit>]
  noscl setprivate <key>
  noscl sign <event-json>
  noscl verify <event-json>
  noscl public
  noscl publish [--reference=<id>...] [--profile=<id>...] [--file=<file>] [<content>]
  noscl message [--reference=<id>...] <pubkey> <content>
  noscl metadata --name=<name> [--about=<about>] [--picture=<picture>] [--nip05=<nip05>] [--banner=<banner>] [--displayname=<displayname>] [--lud16=<lud16>] [--username=<username>] [--website=<website>]
  noscl profile [--verbose] [--json] <pubkey>
  noscl follow <pubkey> [--name=<name>]
  noscl unfollow <pubkey>
  noscl following
  noscl event view [--verbose] [--json] <id>
  noscl event delete <id>
  noscl share-contacts
  noscl key-gen
  noscl relay
  noscl relay add <url>
  noscl relay remove [--all]
  noscl relay remove <url>
  noscl relay recommend <url>
  noscl relay getonline

Specify <content> as '-' to make the publish or message command read it
from stdin.
'''




def main():
    setup_logging()
    logger = logging.getLogger("nospy")

    global config
    config = Config()

    # data_dir = str(Path.home() / DATA_DIR)
    # os.makedirs(data_dir, exist_ok=True)

    # # Parse config
    # config_path = os.path.join(data_dir, CONFIG_FILENAME)
    # if not os.path.exists(config_path):
    #     save_config(config_path)
    # else:
    #     config_init(config_path)


    args = docopt.docopt(USAGE, version=f"nospy {VERSION}")
    # logger.debug(f"args: {args}")

    passed_args = {k: v for k, v in args.items() if v not in (False, [], None)}
    logger.debug(f"passed args: {passed_args}")

    if args["home"]:
        home(args)
    elif args["setprivate"]:
        set_private_key(args)
        config.save_config() #TODO NOT TESTED!!!
        # save_config(config_path)
    elif args["public"]:
        show_public_key(args)
    elif args["key-gen"]:
        key_gen(args)



# if __name__ == '__main__':
#     main()







# NOTE: This is an example of the args dictionary that is returned by docopt.
# args: {'--about': None,
#  '--all': False,
#  '--banner': None,
#  '--displayname': None,
#  '--file': None,
#  '--json': False,
#  '--kinds': [],
#  '--limit': None,
#  '--lud16': None,
#  '--name': None,
#  '--nip05': None,
#  '--noreplies': False,
#  '--onlyreplies': False,
#  '--picture': None,
#  '--profile': [],
#  '--reference': [],
#  '--since': None,
#  '--until': None,
#  '--username': None,
#  '--verbose': False,
#  '--website': None,
#  '<content>': None,
#  '<event-json>': None,
#  '<id>': None,
#  '<key>': None,
#  '<pubkey>': None,
#  '<url>': None,
#  'add': False,
#  'delete': False,
#  'event': False,
#  'follow': False,
#  'following': False,
#  'getonline': False,
#  'home': True,
#  'inbox': False,
#  'key-gen': False,
#  'message': False,
#  'metadata': False,
#  'profile': False,
#  'public': False,
#  'publish': False,
#  'recommend': False,
#  'relay': False,
#  'remove': False,
#  'setprivate': False,
#  'share-contacts': False,
#  'sign': False,
#  'unfollow': False,
#  'verify': False,
#  'view': False}
