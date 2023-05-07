import time
import uuid
import ssl
import json
from nostr.event import EventKind
from nostr.relay_manager import RelayManager
from nostr.key import PublicKey
from nostr.filter import Filter, Filters
from nostr.message_type import ClientMessageType

def get_info():
    pub_key = PublicKey.from_npub('npub1xegedgkkjf24pl4d76cdwhufacng5hapzjnrtgms3pyhlvmyqj9suym08k')
    filters = Filters([Filter(authors=[pub_key.hex()], kinds=[EventKind.SET_METADATA])]) # TEXT_NOTE
    subscription_id = uuid.uuid1().hex

    request = [ClientMessageType.REQUEST, subscription_id]
    request.extend(filters.to_json_array())

    relay_manager = RelayManager()
    # relay_manager.add_relay("wss://nostr-pub.wellorder.net")
    # relay_manager.add_relay("wss://relay.snort.social")
    relay_manager.add_relay("wss://relay.damus.io")
    relay_manager.add_subscription(subscription_id, filters)
    relay_manager.open_connections({"cert_reqs": ssl.CERT_NONE})
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

if __name__ == "__main__":
    get_info()
