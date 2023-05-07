import time
import uuid
import ssl
import json
import re

import logging
logger = logging.getLogger("nospy")

from nostr.event import EventKind
from nostr.relay_manager import RelayManager
from nostr.key import PublicKey
from nostr.filter import Filter, Filters
from nostr.message_type import ClientMessageType

from nospy.config import Config



def get_info(opts):
    input_pubkey = opts.get("<pubkey>", None)
    logger.debug(f"Getting info for {input_pubkey}")

    if input_pubkey.startswith("npub"):
        input_pubkey = PublicKey.from_npub(input_pubkey).hex()
        logger.debug("Converting given npub to hex")
    elif re.match("^[0-9a-fA-F]+$", input_pubkey):
        logger.debug("Given pubkey is already hex - no conversion needed")
    else:
        logger.error("Given pubkey is not valid")
        return

    filters = Filters([Filter(authors=[input_pubkey], kinds=[EventKind.SET_METADATA])])
    subscription_id = uuid.uuid1().hex

    request = [ClientMessageType.REQUEST, subscription_id]
    request.extend(filters.to_json_array())

    logger.debug(f"Request: {request}")

    relay_manager = RelayManager()

    relays = Config.get_instance().relays
    if relays == {}:
        logger.error("You need to add a relay to run 'home'")
        # print("You need to add a relay to run 'home'")
        return

    for relay_url, contents in relays.items():
        if contents['read'] == True:
            logger.debug(f"Adding relay: {relay_url}")
            relay_manager.add_relay(relay_url)
        else:
            logger.debug(f"Skipping non-read relay: {relay_url}")

    # relay_manager.add_relay("wss://relay.damus.io")
    relay_manager.add_subscription(subscription_id, filters)
    relay_manager.open_connections({"cert_reqs": ssl.CERT_NONE}) # NOTE: This disables ssl certificate verification
    time.sleep(1.25) # allow the connections to open

    message = json.dumps(request)
    relay_manager.publish_message(message)
    time.sleep(1) # allow the messages to send

    while relay_manager.message_pool.has_events():
        event_msg = relay_manager.message_pool.get_event()

        data = json.loads(event_msg.event.content)
        pretty_json = json.dumps(data, indent=4)
        print(pretty_json)
    
    relay_manager.close_connections()
