import logging
logger = logging.getLogger("nospy")

from nospy.config import Config

from nostr.key import PrivateKey

def show_private_key(opts):
    if Config.get_instance().private_key is None:
        logger.warn("No private key set.")
        return
    
    # bitz = bytes.fromhex(Config.get_instance().private_key)
    # priv = PrivateKey(bitz)
    priv = Config.get_instance().private_key

    print(f"bech32: {priv.bech32()}")
    print(f"hex:    {priv.hex()}")
