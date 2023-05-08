import logging
logger = logging.getLogger("nospy")

# TODO
from bitcoin import random_key


# from nostr.key import PrivateKey, PublicKey
# TODO tragic.. this needs to be pulled into the nostr library..!
from nospy.keithmukai import Bip39PrivateKey


def format_seed_words(words, num_columns=3):
    num_words = len(words)
    words_per_column = (num_words + num_columns - 1) // num_columns
    max_number_width = len(str(num_words))

    # Calculate the maximum word length in each column
    max_word_lengths = [0] * num_columns
    for col in range(num_columns):
        start = col * words_per_column
        end = min((col + 1) * words_per_column, num_words)
        max_word_lengths[col] = max(len(words[i]) for i in range(start, end))

    formatted_words = ""
    for row in range(words_per_column):
        line = ""
        for col in range(num_columns):
            index = row + col * words_per_column
            if index < num_words:
                number = f"{index + 1:>{max_number_width}}"
                word = words[index].ljust(max_word_lengths[col])
                line += f"{number}. {word}  "
        formatted_words += line.rstrip() + "\n"

    return formatted_words



def key_gen(opts):
    """ Generates a random key with optional supplied-passphrase
    TODO: allow it to randomly generate a passphrase as well?

    Usage:

    ```
    > nospy key-gen [--12-words] [--passphrase=<passphrase>] [--raw]

    --12-words          : Generate a key as 12 seed words (defaults is 24)
    --passphrase=       : Supply a passphrase
    --noformat               : Only display bech32 'nsec' and word list

    ```
    """
    len = 24
    if opts.get("--12-words", False):
        logger.debug("Generating a 12-word mnemonic, instead of 24")
        len = 12
    
    if opts.get("--passphrase", False):
        passphrase = opts["--passphrase"]
        logging.debug(f"Using supplied passphrase: '{passphrase}'")
    else:
        passphrase = None
        logging.debug("no supplied passphrase")

    noformat = False
    if opts.get("--noformat", False):
        noformat = True


    # The key is created right here!
    pk = Bip39PrivateKey.with_mnemonic_length( len )

    # if we're using a passphrase, we need to take the mnemonic of the key we just created and create a new key with the user-supplied passphrase
    if passphrase:
        pk = Bip39PrivateKey(pk.mnemonic, passphrase)

    # mnemonic = " ".join(pk.mnemonic)

    formatted_seed_words = format_seed_words(pk.mnemonic)

    if not noformat:
        print(f"nsec:     {pk.bech32()}")
        print(f"nsec hex: {pk.hex()}")
        print(f"npub:     {pk.public_key.bech32()}")
        print(f"npub hex: {pk.public_key.hex()}")
        print()
        print(" ".join(pk.mnemonic))
        print(formatted_seed_words)
        if passphrase:
            print(f"passphrase:   {passphrase}")
            print(f"with quotes: '{passphrase}'")
    else:
        print(pk.bech32())
        print(pk.hex())
        print(pk.public_key.bech32())
        print(pk.public_key.hex())
        print(" ".join(pk.mnemonic))
        if passphrase:
            print(passphrase)