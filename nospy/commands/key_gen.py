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



def key_gen(opts):
    # Implement nip06.GenerateSeedWords() or find an alternative library
    # seed_words, err = nip06.GenerateSeedWords()
    # if err:
    #     logging.error(err)
    #     return

    # Implement nip06.SeedFromWords() or find an alternative library
    # seed = nip06.SeedFromWords(seed_words)

    # Implement nip06.PrivateKeyFromSeed() or find an alternative library
    # sk, err = nip06.PrivateKeyFromSeed(seed)
    # if err:
    #     logging.error(err)
    #     return

    # Generate a random private key as an alternative
    sk = random_key()

    # print("seed:", seed_words)
    print("private key:", sk)
