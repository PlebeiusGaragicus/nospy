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

    if opts.get("--random", False):
        keyraw = random_key()
        logger.debug(f"Generated a random private key: {keyraw}")
    else:
        keyraw = opts["<key_material>"]
        logger.debug(f"Setting private key to '{keyraw}'")


    # keyval = decode_key(keyraw)

    # config.private_key = keyval

    # logger.debug(f"private_key: {config.private_key}")
