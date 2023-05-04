import os
import logging
from pathlib import Path
import docopt

from nospy import USAGE, VERSION
from nospy.config import config, Config
from nospy.logger import setup_logging

# COMMANDS:
from nospy.commands.home import home
# ...
from nospy.commands.setprivate import set_private_key
from nospy.commands.public import show_public_key
from nospy.commands.key_gen import key_gen



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
        save_config(config_path)
    elif args["public"]:
        show_public_key(args)
    elif args["key-gen"]:
        key_gen(args)



if __name__ == '__main__':
    main()
