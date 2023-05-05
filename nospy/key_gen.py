import logging
logger = logging.getLogger("nospy")

# TODO
from bitcoin import random_key


# from nostr.key import PrivateKey, PublicKey
# TODO tragic.. this needs to be pulled into the nostr library..!
from nospy.keithmukai import Bip39PrivateKey



def key_gen(opts):
    """ Generates a random key with optional supplied-passphrase
    TODO: allow it to randomly generate a passphrase as well?

    Usage:

    ```
    > nospy key-gen [--12-words] [--passphrase=<passphrase>] [--raw]

    --12-words          : Generate a key as 12 seed words (defaults is 24)
    --passphrase=       : Supply a passphrase
    --raw               : Do not label the key outputs
    --nolabels          : Do not label the key outputs (TODO - rename???)

    ```
    """
    len = 24
    if opts.get("--12-words", False):
        logger.debug("Generating a 12-word mnemonic, instead of 24")
        len = 12
    
    if opts.get("--passphrase", False):
        passphrase = opts["--passphrase"]
        logging.debug(f"Using supplied passphrase: '{passphrase}'")
    else:
        passphrase = None
        logging.debug("no supplied passphrase")

    raw = False
    if opts.get("--raw", False):
        raw = True


    # The key is created right here!
    pk = Bip39PrivateKey.with_mnemonic_length( len )

    # if we're using a passphrase, we need to take the mnemonic of the key we just created and create a new key with the user-supplied passphrase
    if passphrase:
        pk = Bip39PrivateKey(pk.mnemonic, passphrase)

    #
    mnemonic = " ".join(pk.mnemonic)

    if not raw:
        print(f"nsec:       {pk.bech32()}")
        print(f"nsec hex:   {pk.hex()}")
        print(f"bech32:     {pk.public_key.bech32()}")
        print(f"bech32 hex: {pk.public_key.hex()}")
        print(f"seed words: {mnemonic}")
        if passphrase:
            print(f"passphrase: {passphrase}")
            print(f"w/ quotes: '{passphrase}'")
    else:
        print(pk.bech32())
        print(pk.hex())
        print(pk.public_key.bech32())
        print(pk.public_key.hex())
        print(mnemonic)
        if passphrase:
            print(passphrase)
