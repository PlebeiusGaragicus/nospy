import sys
import re
import logging
logger = logging.getLogger("nospy")


import codecs
import logging
from bech32 import decode
from bitcoin import ecdsa_raw_sign
from bitcoin import privtopub
from bitcoin import random_key
from docopt import docopt


from nospy import config
from nospy.keys import decode_key


def set_private_key(opts):
    """ Set the private key.
    Note: this function has no side effects - you'll need to save the config after calling it.
        This function will fail and exit() for unrecoverable errors.

    ```
    Usage:
        nospy setprivate nsec1234567890... # BASE58 nsec
        nospy setprivate 893ho383hjal39... # HEX ENCODED
        nospy setprivate abandon abando... # SEED WORDS
        nospy setprivate --random          # Generate a random key
    ```

    """

    # if the user wants to generate a random key
    if opts.get("--random", False):
        keyraw = random_key()
        logger.debug(f"Generated a random private key: {keyraw}")
    
        # if the user supplies key material
    else:
        keyraw = opts["<key_material>"]
        logger.debug(f"Setting private key to '{keyraw}'")

        # Check if keyraw is a valid BASE58 nsec string
        if re.match("^nsec[1-9A-HJ-NP-Za-km-z]+$", keyraw):
            logging.debug(f"BASE58 nsec string detected: {keyraw}")
            # TODO: Process the BASE58 nsec string
            pass

        # Check if keyraw is a valid hex-encoded string
        elif re.match("^[0-9a-fA-F]+$", keyraw):
            logging.debug(f"Hex-encoded string detected: {keyraw}")
            # TODO: Process the hex-encoded string
            pass

        # If keyraw is neither BASE58 nsec nor hex-encoded, assume it's a list of seed words
        else:
            seed_words = keyraw.split()
            logging.debug(f"Seed words detected: {seed_words}")
            # TODO: Process the seed words
            pass
