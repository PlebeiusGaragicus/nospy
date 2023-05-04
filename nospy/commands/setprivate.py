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
from nospy.keys import decode_key, get_pub_key



def set_private_key(opts):
    """ TODO
    Set the private key
    """
    logger.debug(f"Setting private key to '{opts['<key>']}'")

    keyraw = opts["<key>"]
    keyval = decode_key(keyraw)

    # config.config["private_key"] = opts["<key>"]
    config[PRIVATE_KEY] = keyval.decode()

    logger.debug(f"private_key: {config.config['private_key']}")
