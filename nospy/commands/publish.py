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

from nospy.relay import connect_to_relays


def init_nostr():
    logger.debug("Initializing Nostr...")




def publish(args):
    """ Publishes a message to the network.
    TODO
    
    Usage:
    ```
    nospy publish [<content>] [--file=<file>]
    ```

    """
    content = args.get('<content>', None)
    file_path = args.get('--file', None)

    if file_path:
        logger.debug(f"Reading content from file: '{file_path}'")
        try:
            with open(file_path, "r") as file:
                content = file.read()
        except IOError as e:
            logger.error(f"Error reading file: {e}")
            return
    elif content == '-':
        logger.debug(f"Reading content from stdin...")
        content = sys.stdin.read()
    else:
        logger.debug(f"Using content from argument: {content}")

    if not content or content == "":
        logger.error("No content provided. Content must not be empty.")
        return
    
    relay_manager = connect_to_relays()

    priv = Config.get_instance().private_key
    event = Event(priv.public_key.hex(), content)
    priv.sign_event(event)

    logger.debug("Publishing event...")
    relay_manager.publish_event(event)
    time.sleep(1) # allow the messages to send

    relay_manager.close_connections()
