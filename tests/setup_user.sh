#!/bin/bash

# SET THE USER
NOSPY_USER=#TODO

# SET THE PRIVATE KEY
PRIVATE=$(nospy keygen | grep -m 1 'nsec:' | awk '{print $2}')
nospy setprivate $PRIVATE

# ADD RELAYS
nospy relay-add wss://relay.damus.io
nospy relay-add wss://nos.lol
nospy relay-add wss://relay.snort.social

# ADD MEDIA TO NOSTR.BUILD
#TODO upload
nospy upload <PROFILE>
# TODO: WHAT ABOUT UPLOAD ERRORS?
# CAPTURE THIS

nospy upload <BANNER>
# CAPTURE THIS


nospy setprofile <...> <...>
