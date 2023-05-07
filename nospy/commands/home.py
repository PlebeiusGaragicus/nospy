import json
import time
import uuid
import ssl
import datetime
import logging
logger = logging.getLogger("nospy")

from nostr.filter import Filter, Filters
from nostr.event import Event, EventKind
from nostr.relay_manager import RelayManager
from nostr.message_type import ClientMessageType
from nostr.key import PublicKey

from nospy.config import Config
from nospy.keys import npubToHex


def print_event(event, name: str, verbose: bool, json_format: bool):
    # print(f"{nick}:", end=" ")
    # if json_format:
    #     print(json.dumps(event.to_dict()))
    # else:
    #     print(event)
    # data = json.loads(event_msg.event.content)
    # pretty_json = json.dumps(data, indent=4)
    # print(pretty_json)

    dt = datetime.datetime.fromtimestamp(event.event.created_at).strftime('%Y-%m-%d %H:%M')

    blue = "\033[1;34m"
    green = "\033[0;32m"
    end = "\033[0m"

    print(f"{dt} | {blue}{name}{end}:", end=" ")
    print(f"{green}{event.event.content}{end}")


def home(opts, inbox_mode=False):
    if len(Config.get_instance().following) == 0:
        print("You need to be following someone to run 'home'")
        return

    # get the list of npubs we are following...
    following = Config.get_instance().following

    # look for any entries that don't have a name, and give them a name (e.g. npub18~a2xw)
    for npub, f in following.items():
        if f['name'] is None:
            f['name'] = f"{npub[:6]}~{npub[-4:]}"

    # convert the dict so that the public keys are hex-encoded - because that's what the relay manager expects
    hex_following = {npubToHex(pubkey): info for pubkey, info in following.items()}

    # This is our filter the tells the relay what we're looking for
    filters = Filters([Filter(authors=list(hex_following.keys()), kinds=[EventKind.TEXT_NOTE])]) # TEXT_NOTE
    subscription_id = uuid.uuid1().hex

    # create a relay manager and add our relays
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

    relay_manager.add_subscription(subscription_id, filters)
    relay_manager.open_connections({"cert_reqs": ssl.CERT_NONE}) # NOTE: This disables ssl certificate verification

    # create a request message to send to the relay
    request = [ClientMessageType.REQUEST, subscription_id]
    request.extend(filters.to_json_array())
    message = json.dumps(request)

    # send the request to the relay
    time.sleep(1.25) # allow the connections to open
    relay_manager.publish_message(message) # send the request to the relay
    time.sleep(1) # allow the messages to send

    # now, with our subscription in place, we can start listening for events
    try:
        while True:
            # TODO: check if the websocket closes.. and reopen if needed.
            # TODO: I should probably break this up into a few functions...
            while relay_manager.message_pool.has_events():
                event_msg = relay_manager.message_pool.get_event()

                from_pub = event_msg.event.public_key
                name = hex_following[from_pub]['name'] # look up the name we gave this person

                print_event(event_msg, name, verbose=False, json_format=False)

    except KeyboardInterrupt:
        relay_manager.close_connections()
        print("\nClosing connections...")

    # relay_manager.close_connections()
