**NOTE**: This is totally a work-in-progress.  My goal is to bring this to feature parity with `noscl` before I ever reach out to anyone about it.

# nospy

A [nostr](https://github.com/fiatjaf/nostr) command-line utility written in Python: **NOS**tr **PY**thon

Fiatjaf's `noscl` is _really_ cool, but I don't know Go.  So, I'm doing things the hard way... I mean the fun way... 😘

The article that started it all: https://dergigi.com/2023/01/19/how-to-build-a-nostr-gm-bot/

# Usage:

```
Usage:
  nospy version
  nospy setprivate <key>
  nospy public
  nospy publish
  nospy follow <pubkey> [--name=<name>]
  nospy unfollow <pubkey>
  nospy following
  nospy key-gen
```

# How to install

`git clone` this repo and run `pip install -e .` inside the created directory.

Then, you should be able to run `nospy`


# Reference

- https://github.com/fiatjaf/noscl
- https://github.com/nostr-protocol/nips
