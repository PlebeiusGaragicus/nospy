import logging
logger = logging.getLogger("nospy")

from nospy.config import Config

from nostr.key import PrivateKey

def show_public_key(opts):
    if Config.get_instance().private_key is None:
        logger.warn("No private key set.")
        return
    
    # bitz = bytes.fromhex(Config.get_instance().private_key)
    # priv = PrivateKey(bitz)
    pub = Config.get_instance().public_key

    print(f"bech32: {pub.bech32()}")
    print(f"hex:    {pub.hex()}")
