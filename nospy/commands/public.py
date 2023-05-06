import logging
logger = logging.getLogger("nospy")

from nospy.config import Config

from nostr.key import PrivateKey

def show_public_key(opts):
    if Config.get_instance().private_key == None:
        logger.warn("No private key set.")
        return
    
    bitz = bytes.fromhex(Config.get_instance().private_key)

    priv = PrivateKey(bitz)

    print(f"npub: {priv.public_key.bech32()}")
    print(f"hex:  {priv.public_key.hex()}")
