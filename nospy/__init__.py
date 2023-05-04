VERSION = '0.0.1'

USAGE = '''
noscl

Usage:
  noscl home [--verbose] [--json] [--onlyreplies] [--noreplies] [--kinds=<kinds>...] [--since=<since>] [--until=<until>] [--limit=<limit>]
  noscl inbox [--verbose] [--json] [--onlyreplies] [--noreplies] [--since=<since>] [--until=<until>] [--limit=<limit>]
  noscl setprivate <key>
  noscl sign <event-json>
  noscl verify <event-json>
  noscl public
  noscl publish [--reference=<id>...] [--profile=<id>...] [--file=<file>] [<content>]
  noscl message [--reference=<id>...] <pubkey> <content>
  noscl metadata --name=<name> [--about=<about>] [--picture=<picture>] [--nip05=<nip05>] [--banner=<banner>] [--displayname=<displayname>] [--lud16=<lud16>] [--username=<username>] [--website=<website>]
  noscl profile [--verbose] [--json] <pubkey>
  noscl follow <pubkey> [--name=<name>]
  noscl unfollow <pubkey>
  noscl following
  noscl event view [--verbose] [--json] <id>
  noscl event delete <id>
  noscl share-contacts
  noscl key-gen
  noscl relay
  noscl relay add <url>
  noscl relay remove [--all]
  noscl relay remove <url>
  noscl relay recommend <url>
  noscl relay getonline

Specify <content> as '-' to make the publish or message command read it
from stdin.
'''

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
