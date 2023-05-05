import os
import sys
from pathlib import Path
import logging
import json
from dataclasses import dataclass, field

logger = logging.getLogger("nospy")

# This is the global config object that is set in __main__.py
config = None

DATA_DIR = ".config/nospy"
CONFIG_FILENAME = "config.json"


@dataclass
class Config:
    # file_name: str = CONFIG_FILENAME
    state: dict = field(default_factory=dict)

    def __post_init__(self):
        # data_dir = str(Path.home() / DATA_DIR)
        # TODO: This is a hack to allow for testing. We should find a better way to do this.... also... don't ship this code with this hack in it...
        if os.getenv("DEBUG", False):
            data_dir = str(Path.cwd() / DATA_DIR)
        else:
            data_dir = str(Path.home() / DATA_DIR)
        os.makedirs(data_dir, exist_ok=True)

        # Parse config
        self.config_path = os.path.join(data_dir, CONFIG_FILENAME)
        # NOTE: There is no reason to save an empty config file... also, we can't do this inside __init__ because self.state isn't set yet
        # if not os.path.exists(config_path):
        #     logging.warn(f"Config file not found. Creating a new one: {config_path}")
        #     self.save_config(config_path)
        # else:
        #     self.load_config(config_path)
        if os.path.exists(self.config_path):
            self.load_config()


    ##############################
    @property
    def private_key(self):
        return self.state.get("private_key")

    @private_key.setter
    def private_key(self, value):
        self.state["private_key"] = value
    ##############################


    def save_config(self):
        """Save the config file."""

        data_dir = str(Path.home() / DATA_DIR)
        os.makedirs(data_dir, exist_ok=True)

        with open(self.config_path, "w") as f:
            json.dump(self.state, f, indent=4)

        logger.debug(f"Saving the current config to file: {self.config_path}")
        logger.debug(f"Config: {self.state}")


    def load_config(self):
        """Initialize the config file."""
        logger.debug(f"Loading config file: {self.config_path}")

        with open(self.config_path, "r") as f:
            try:
                self.state = json.load(f)
                logger.debug(f"Config: {self.state}")
            except json.JSONDecodeError as e:
                logger.critical(f"Can't parse config file. Ensure the file is properly formatted JSON. {self.config_path}: {str(e)}")
                sys.exit(1)
