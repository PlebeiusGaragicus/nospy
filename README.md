**NOTE**: This is totally a work-in-progress.  My goal is to bring this to feature parity with `noscl` but that may take awhile.

It works for now 🤷

# nospy

A [nostr](https://github.com/fiatjaf/nostr) command-line utility written in Python: **NOS**tr **PY**thon

Fiatjaf's `noscl` is [_really_ cool](https://github.com/fiatjaf/noscl), but I don't know Go.  So, I'm doing things the hard way... I mean the fun way!

The article that inspired me: https://dergigi.com/2023/01/19/how-to-build-a-nostr-gm-bot/

# Usage:

```
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
  nospy users
  nospy upload <file>
```

`nospy` is now mult-user capable.  User config files are stored in `~/.config/nospy/<username>.json`. To use `nospy` with a user set the NOSPY_USER environment variable.  If NOSPY_USER is not set, then the 'default' user will be used.

# How to install

```sh
git clone https://github.com/PlebeiusGaragicus/nospy.git
cd nospy
pip install -r requirements.txt
pip install .

# verify install
which nospy
nospy version
```

# Reference

- https://github.com/fiatjaf/noscl
- https://github.com/nostr-protocol/nips
