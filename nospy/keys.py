import logging
logger = logging.getLogger("nospy")

from typing import Union

from nostr.key import PrivateKey

import bech32

from nospy.config import Config


#  A Bech32_encoded address consists of 3 parts: HRP + Separator + Data: bc1qw508d6qejxtdg4y5r3zarvary0c5xw7kv8f3t4
# https://en.bitcoin.it/wiki/Bech32
def nsecToHex(nsec: str) -> Union[None, str]:
    """ provide a bech32 nsec-formatted string, and get back the hex-encoded private key """

    # Decode the BASE58 nsec string
    # keyval = bech32.decode(keyraw)
    # keyval = bech32.bech32_decode(keyraw)

    # hrpgot, data = bech32.bech32_decode("nsec", keyraw.split("nsec")[1])
    hrpgot, data = bech32.bech32_decode(nsec)

    if hrpgot != "nsec":
        logger.critical("Invalid human-readable part (prefix) of the encoded private key.")
        return None
        # raise ValueError("Invalid human-readable part (prefix) of the encoded private key.")

    decoded = bech32.convertbits(data, 5, 8, False)
    if decoded is None:
        logger.critical("Error decoding the encoded private key.")
        return None
        # raise ValueError("Error decoding the encoded private key.")

    keyval = ''.join('{:02x}'.format(byte) for byte in decoded)

    return keyval


    # return bech32.decode(nsec).data.toString('hex');








def load_private_key() -> Union[None, PrivateKey]:
    Config.get_instance().load_config()

    privkey = Config.get_instance().private_key

    if not privkey:
        logger.critical("No private key found. Please set a private key first.")
        return None
    
    bs = bytes.fromhex(privkey)

    return PrivateKey(bs)







# def decode_key(keyraw: str): 
#     if len(keyraw) == 64:
#         # hex-encoded
#         try:
#             keyval = codecs.decode(keyraw, "hex")
#         except ValueError as e:
#             raise ValueError(f"Decoding key from hex: {str(e)}") from e
#         return keyval
#     else:
#         # bech32-encoded
#         _, keyval = bech32.decode(keyraw)
#         if keyval is None:
#             raise ValueError(f"Decoding key from bech32: invalid bech32 string")
#         return bytes(keyval)




# def get_pub_key(private_key: str):
#     try:
#         pubkey = privtopub(private_key)
#     except Exception as e:
#         logging.info(f"Error decoding key from hex: {str(e)}")
#         return ""
#     return pubkey

