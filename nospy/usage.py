# NOTE: This usage string is very important.  Since we are using docopt, it is used to parse the command line arguments.
USAGE = '''
Usage:
  nospy version
  nospy setprivate <key_material> [--passphrase=<passphrase>]
  nospy public
  nospy private
  nospy publish [<content>] [--file=<file>]
  nospy follow <pubkey> [--name=<name>]
  nospy unfollow <pubkey>
  nospy following
  nospy getinfo <pubkey>
  nospy home
  nospy keygen [--12-words] [--passphrase=<passphrase>] [--noformat]
  nospy relay-add <url>
  nospy relay-remove [<url> | --all]
  nospy relays

Notes:
  <key_material> for the setprivate command can be:
    - A nsec (base58) string (e.g., nsec1234567890...)
    - A hex-encoded string (e.g., 1a2b3c4d...)
    - A list of seed words enclosed in quotes (e.g., "word1 word2 word3 ...")
'''



# # NOTE: This usage string is very important.  Since we are using docopt, it is used to parse the command line arguments.
# USAGE = '''
# nospy

# Usage:
#   nospy home [--verbose] [--json] [--onlyreplies] [--noreplies] [--kinds=<kinds>...] [--since=<since>] [--until=<until>] [--limit=<limit>]
#   nospy inbox [--verbose] [--json] [--onlyreplies] [--noreplies] [--since=<since>] [--until=<until>] [--limit=<limit>]
#   nospy setprivate <key>
#   nospy sign <event-json>
#   nospy verify <event-json>
#   nospy public
#   nospy publish [--reference=<id>...] [--profile=<id>...] [--file=<file>] [<content>]
#   nospy message [--reference=<id>...] <pubkey> <content>
#   nospy metadata --name=<name> [--about=<about>] [--picture=<picture>] [--nip05=<nip05>] [--banner=<banner>] [--displayname=<displayname>] [--lud16=<lud16>] [--username=<username>] [--website=<website>]
#   nospy profile [--verbose] [--json] <pubkey>
#   nospy follow <pubkey> [--name=<name>]
#   nospy unfollow <pubkey>
#   nospy following
#   nospy event view [--verbose] [--json] <id>
#   nospy event delete <id>
#   nospy share-contacts
#   nospy key-gen
#   nospy relay
#   nospy relay add <url>
#   nospy relay remove [--all]
#   nospy relay remove <url>
#   nospy relay recommend <url>
#   nospy relay getonline

# Specify <content> as '-' to make the publish or message command read it
# from stdin.
# '''






# NOTE: This is an example of the args dictionary that is returned by docopt.
# args: {'--about': None,
#  '--all': False,
#  '--banner': None,
#  '--displayname': None,
#  '--file': None,
#  '--json': False,
#  '--kinds': [],
#  '--limit': None,
#  '--lud16': None,
#  '--name': None,
#  '--nip05': None,
#  '--noreplies': False,
#  '--onlyreplies': False,
#  '--picture': None,
#  '--profile': [],
#  '--reference': [],
#  '--since': None,
#  '--until': None,
#  '--username': None,
#  '--verbose': False,
#  '--website': None,
#  '<content>': None,
#  '<event-json>': None,
#  '<id>': None,
#  '<key>': None,
#  '<pubkey>': None,
#  '<url>': None,
#  'add': False,
#  'delete': False,
#  'event': False,
#  'follow': False,
#  'following': False,
#  'getonline': False,
#  'home': True,
#  'inbox': False,
#  'key-gen': False,
#  'message': False,
#  'metadata': False,
#  'profile': False,
#  'public': False,
#  'publish': False,
#  'recommend': False,
#  'relay': False,
#  'remove': False,
#  'setprivate': False,
#  'share-contacts': False,
#  'sign': False,
#  'unfollow': False,
#  'verify': False,
#  'view': False}
