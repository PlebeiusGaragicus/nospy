import os
import sys
import json
from pathlib import Path
from dataclasses import dataclass, field
from typing import Union

import logging
logger = logging.getLogger("nospy")

from nostr.key import PrivateKey, PublicKey

DATA_DIR = ".config/nospy"
CONFIG_FILENAME = "config.json"


class Singleton:
    _instance = None

    def __init__(self):
        # Singleton pattern must prevent normal instantiation
        raise Exception("Cannot directly instantiate a Singleton. Access via get_instance()")

    @classmethod
    def get_instance(cls):
        # This is the only way to access the one and only instance
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            cls._instance.__post_init__() # __post_init__() is needed becuase Config is a dataclass
        return cls._instance



@dataclass
class Config(Singleton):
    state: dict = field(default_factory=dict)

    def __post_init__(self):
        # logger.debug("Initializing config...")
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

        self.load_config()

        # if os.path.exists(self.config_path):
        #     self.load_config()
        # else:
        #     # logger.warn(f"Config file not found. Creating a new one: {self.config_path}")
        #     logger.warn(f"Config file not found.")
            # self.save_config()


    ##############################
    # @property
    # def private_key(self):
    #     return self.state.get("private_key")
    @property
    def private_key(self) -> Union[None, PrivateKey]:
        priv = self.state.get("private_key", None)
        if priv is None:
            return None
        bites = bytes.fromhex(priv)
        return PrivateKey(bites)

    @private_key.setter
    def private_key(self, key): # TODO: -> None ??? SHOULD A DATACLASS SETTER HAVE A RETURN TYPE?  -> Config (????)
        self.state["private_key"] = key

    @property
    def public_key(self) -> Union[None, PublicKey]:
        priv = self.private_key
        if priv is None:
            return None
        return priv.public_key

    @property
    def relays(self) -> dict:
        return self.state.get("relays", {})
    
    def add_relay(self, addr, policy) -> None:
        if "relays" not in self.state:
            self.state["relays"] = {}
        self.state["relays"][addr] = policy

    def remove_relay(self, addr) -> bool:
        if "relays" in self.state and addr in self.state["relays"]:
            del self.state["relays"][addr]
            return True
        else:
            return False
        
    def clear_relays(self) -> None:
        self.state["relays"] = {}

    @property
    def following(self) -> dict:
        return self.state.get("following", {})

    # def follow(self, pubkey, nickname=None):
    #     if "following" not in self.state:
    #         self.state["following"] = []

    #     f = {
    #             "pubkey": pubkey,
    #             "nickname": nickname
    #          }

    #     self.state["following"].append(f)

    # def unfollow(self, addr) -> bool:
    #     if "following" in self.state and addr in self.state["following"]:
    #         self.state["following"].remove(addr)
    #         return True
    #     else:
    #         return False

    def follow(self, pubkey, name=None) -> None:
        if "following" not in self.state:
            self.state["following"] = {}

        self.state["following"][pubkey] = {"name": name}

    def unfollow(self, pubkey) -> bool:
        if "following" in self.state and pubkey in self.state["following"]:
            del self.state["following"][pubkey]
            return True
        else:
            return False
            
    
    ##############################


    def save_config(self):
        """Save the config file."""

        data_dir = str(Path.home() / DATA_DIR)
        os.makedirs(data_dir, exist_ok=True)

        with open(self.config_path, "w") as f:
            json.dump(self.state, f, indent=4)

        logger.debug(f"Saving the current config to file: {self.config_path}")
        # logger.debug(f"Config: {self.state}")


    def load_config(self):
        """Initialize the config file."""
        logger.debug(f"Loading config file: {self.config_path}")

        if not os.path.exists(self.config_path):
            logger.warn(f"Config file not found.")
            self.state = {} # Set the state to an empty dictionary
            return

        if os.path.getsize(self.config_path) == 0:
            logger.warn(f"Config file is empty.")
            self.state = {}  # Set the state to an empty dictionary
            return

        with open(self.config_path, "r") as f:
            try:
                self.state = json.load(f)
                # logger.debug(f"Config: {self.state}")
            except json.JSONDecodeError as e:
                logger.critical(f"Can't parse config file. Ensure the file is properly formatted JSON. {self.config_path}: {str(e)}")
                sys.exit(1)
