from dataclasses import dataclass
from typing import List
import secrets

from embit import bip39
from embit.bip32 import HDKey
from nostr.key import PrivateKey

# https://github.com/kdmukai/python-nostr/blob/0c0f9040df43cb7a3cd5c72f606322a2322f2a62/nostr/key.py#L120

@dataclass
class Bip39PrivateKey(PrivateKey):
    """
        Nostr PrivateKey that is derived from a BIP-39 mnemonic + optional BIP-39
        passphrase using the derivation path specified in NIP-06.
    """
    mnemonic: List[str] = None
    passphrase: str = None

    def __post_init__(self):
        if self.mnemonic is None:
            self.mnemonic = bip39.mnemonic_from_bytes(secrets.token_bytes(32)).split()
        
        if self.passphrase is None:
            # Per BIP-39 spec, no passphrase is the empty string
            self.passphrase = ""

        # Convert the mnemonic to the root HDKey and derive the Nostr key per NIP-06
        root = HDKey.from_seed(bip39.mnemonic_to_seed(mnemonic=" ".join(self.mnemonic), password=self.passphrase))
        nostr_root = root.derive("m/44h/1237h/0h/0/0")

        super().__init__(raw_secret=nostr_root.secret)
    

    @classmethod
    def with_mnemonic_length(cls, num_words: int):
        """ Creates a new random BIP-39 mnemonic of the specified length to generate a new Nostr PK """
        if num_words == 24:
            # default is already 24 word-mnemonic
            return cls()
        elif num_words == 12:
            # 12-word mnemonic == 16-byte input entropy
            mnemonic = bip39.mnemonic_from_bytes(secrets.token_bytes(16)).split()
            return cls(mnemonic=mnemonic)
        else:
            raise Exception("Only mnemonics of length 12 or 24 are supported")

