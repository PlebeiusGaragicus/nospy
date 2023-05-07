import sys
import ssl
import time
from nostr.event import Event
from nostr.relay_manager import RelayManager
from nostr.message_type import ClientMessageType
from nostr.key import PrivateKey

import logging
logger = logging.getLogger("nospy")

from nospy.config import Config

# relay_manager.add_relay("wss://nostr-pub.wellorder.net")
# relay_manager.add_relay("wss://relay.damus.io")

def connect_to_relays() -> RelayManager:
    relay_manager = RelayManager()
    relays = Config.get_instance().relays
    for r in relays:
        logger.debug(f"Adding relay: {r}")
        relay_manager.add_relay(r)


    logger.debug("Opening connections...")
    relay_manager.open_connections({"cert_reqs": ssl.CERT_NONE}) # NOTE: This disables ssl certificate verification
    time.sleep(1.25) # allow the connections to open

    return relay_manager
