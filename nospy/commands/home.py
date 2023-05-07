import json
import time

import nostr

from nospy.config import Config


def print_event(event, nick: str, verbose: bool, json_format: bool):
    print(f"{nick}:", end=" ")
    if json_format:
        print(json.dumps(event.to_dict()))
    else:
        print(event)


def home(opts, inbox_mode=False):
    if len(Config.get_instance().following) == 0:
        print("You need to be following someone to run 'home'")
        return

    init_nostr()

    verbose = opts.get('--verbose', False)
    json_format = opts.get('--json', False)
    no_replies = opts.get('--noreplies', False)
    only_replies = opts.get('--onlyreplies', False)
    kinds = [int(kind) for kind in opts.get('--kinds', [])]
    since = opts.get('--since', 0)
    until = opts.get('--until', 0)
    limit = opts.get('--limit', 0)

    keys = []
    name_map = {}
    for follow in Config.get_instance().following:
        keys.append(follow['key'])
        if follow['name']:
            name_map[follow['key']] = follow['name']

    pubkey = get_pub_key(config['private_key'])
    filters = [nostr.Filters(limit=limit)]

    if inbox_mode:
        filters[0].tags = {'p': {pubkey}}
        kinds = [nostr.KindEncryptedDirectMessage]
    else:
        filters[0].authors = keys

    if since > 0:
        since_time = time.gmtime(since)
        filters[0].since = since_time

    if until > 0:
        until_time = time.gmtime(until)
        filters[0].until = until_time

    filters[0].kinds = kinds
    _, all_events = pool.sub(filters)

    for event in nostr.unique(all_events):
        nick = name_map.get(event.pub_key, '')

        if not nick and event.kind == nostr.KindSetMetadata:
            metadata = json.loads(event.content)
            nick = metadata['name']
            name_map[nick] = event.pub_key

        if only_replies or no_replies:
            has_references = any(tag[0] == 'e' for tag in event.tags)
            if no_replies and has_references:
                continue
            if only_replies and not has_references:
                continue

        print_event(event, nick, verbose, json_format)
