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



def decode_key(keyraw: str):
    if len(keyraw) == 64:
        # hex-encoded
        try:
            keyval = codecs.decode(keyraw, "hex")
        except ValueError as e:
            raise ValueError(f"Decoding key from hex: {str(e)}") from e
        return keyval
    else:
        # bech32-encoded
        _, keyval = decode(keyraw)
        if keyval is None:
            raise ValueError(f"Decoding key from bech32: invalid bech32 string")
        return bytes(keyval)




def get_pub_key(private_key: str):
    try:
        pubkey = privtopub(private_key)
    except Exception as e:
        logging.info(f"Error decoding key from hex: {str(e)}")
        return ""
    return pubkey
