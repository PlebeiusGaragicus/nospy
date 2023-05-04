import argparse
import json
import logging
import os
# import sys
from pathlib import Path

import docopt

# from config import config_init, save_config
from nospy.home import home

# from nospy import USAGE, __version__
from nospy import USAGE, VERSION

def main():
    # # Find the data directory
    # data_dir = str(Path.home() / ".config/nostr")
    # os.makedirs(data_dir, exist_ok=True)

    # # Logger config
    # logging.basicConfig(level=logging.INFO, format="<> %(message)s")
    # log = logging.getLogger(__name__)

    # # Parse config
    # config_path = os.path.join(data_dir, "config.json")
    # if not os.path.exists(config_path):
    #     save_config(config_path)

    # with open(config_path, "r") as f:
    #     try:
    #         config = json.load(f)
    #     except json.JSONDecodeError as e:
    #         log.error(f"Can't parse config file {config_path}: {str(e)}")
    #         return

    # Initialize config
    # config_init()

    # Parse args
    args = docopt.docopt(USAGE, version=f"nospy {VERSION}")

    print(f"args: {args}")

    # Execute functions based on parsed arguments
    # Replace function names with actual function calls
    if args["home"]:
        home(args)
    else:
        print("Invalid command")
    # elif args["inbox"]:
    #     home(args, True)
    # elif args["setprivate"]:
    #     set_private_key(args)
    #     save_config(config_path)
    # ...






if __name__ == '__main__':
    main()
    print("DONE")
