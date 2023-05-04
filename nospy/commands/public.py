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






def show_public_key(opts):
    if config["PrivateKey"] == "":
        logging.warn("No private key set.")
        return

    pubkey = get_pub_key(config["PrivateKey"])
    if pubkey != "":
        print(pubkey)
        # Implement nip19.EncodePublicKey() or find an alternative library
        # nip19pubkey, _ = nip19.EncodePublicKey(pubkey, "")
        # print(nip19pubkey)

