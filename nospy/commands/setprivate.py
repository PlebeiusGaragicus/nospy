import sys
import re
from typing import Union
import logging
logger = logging.getLogger("nospy")

from bip32 import BIP32
import bip39

from nospy.config import Config
from nospy.keys import nsecToHex
from nospy.keithmukai import Bip39PrivateKey


def set_private_key(opts) -> Union[None, str]:
    """ Set the private key.
    Note: this function has no side effects - you'll need to save the config after calling it.
        This function will fail and exit() for unrecoverable errors.

    ```
    Usage:
        nospy setprivate [--random | <key_material>] [--passphrase=<passphrase>]

        Example: SUPPLY BASE58 NSEC
        > nospy setprivate nsec1fh4tww42zmvt6y5mwt3jdwalmckaz8npaw0sqz25admxk5x2w4kq600yfh

        Example: SUPPLY HEX ENCODED SOMETHING ---(FORMAT NAME??? TODO)
        > nospy setprivate 4deab73aaa16d8bd129b72e326bbbfde2dd11e61eb9f000954eb766b50ca756c

        Example: SUPPLY SEED WORDS WITH OPTIONAL PASSPHRASE
        > nospy setprivate "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon" [--passphrase=abandon]
        # NOTE: ensure seed words are contained inside quotes

        Example: USE A NEW RANDOMLY-GENERATED KEY (WITH OPTIONAL PASSPHRASE)
        nospy setprivate --random [--passphrase="passphrase here"]
    ```
    """
    # if the user wants to generate a random key
    # NOTE: FEATURE REMOVED
    # if opts.get("--random", False):
    #     logger.warn("NOT IMPLEMENTED")
    #     # keyraw = random_key()
    #     # logger.debug(f"Generated a random private key: {keyraw}")
    #     return None



    keyraw = opts["<key_material>"]
    # logger.debug(f"Setting private key to '{keyraw}'")



    # if keyraw is BASE58 nsec
    # if re.match("^nsec", keyraw):
    if keyraw.startswith("nsec"):
        logging.debug(f"BASE58 nsec string detected: {keyraw}")

        priv_hex = nsecToHex(keyraw)
        if not priv_hex:
            logger.error(f"Error decoding nsec: {keyraw}")
        else:
            logger.debug(f"Decoded into hex: {priv_hex}")

        # return ret
        Config.get_instance().private_key = priv_hex
        Config.get_instance().save_config()



    # keyraw is a hex-encoded string
    elif re.match("^[0-9a-fA-F]+$", keyraw):
        # TODO: ERROR CHECKING HERE
        logger.debug(f"Hex-encoded string detected: {keyraw}")
        logger.critical("NOT IMPLEMENTED")
        sys.exit(1)
        # logger.info(f"Supplied hex-encded private key appears valid: {fuck}")



    # If keyraw is neither BASE58 nsec nor hex-encoded, assume it's a list of seed words
    else:
        wordlist = keyraw.split()
        logger.debug(f"Procesing seed words: {wordlist}")

        passphrase = None
        if opts.get("--passphrase", False):
            passphrase = opts["--passphrase"]
            logging.debug(f"Using supplied passphrase: '{passphrase}'")

        # Refer to: https://github.com/nostr-protocol/nips/blob/master/06.md
        # derivation_path = "m/44'/1237'/0'/0/0"
        try:
            pk = Bip39PrivateKey(mnemonic=wordlist, passphrase=passphrase)

            Config.get_instance().private_key = pk.hex()
            Config.get_instance().save_config()
        except bip39.DecodingError as e:
            logger.error(f"{str(e)}")
            sys.exit(1)
            # TODO: should this function exit() or return false or what?
            # return
        except ValueError as e:
            logger.error(f"{str(e)}")
            sys.exit(1)
            # return
