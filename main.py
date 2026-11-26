#!/usr/bin/env python3
"""One-word entry: The Internet in One Word.

The brief asks for one word offered as a description of
the whole internet, funny and fitting at once. A comedy
editor judges pairs of words, weighing, in order: the
entry really is a single word describing the whole
internet, so a phrase, a sentence or a list loses to any
single word that captures it; the word earns a laugh by
itself, with no explanation needed; it says something
true about the internet as a whole rather than one app,
one site or one mood; it surprises, not the first obvious
word anyone would reach for; and it lands in one beat,
spelled correctly, instantly readable, and short enough
to hit before the reader thinks.

The sealed word below follows that order on purpose. It
is a single word, thirteen letters, no spaces and no
punctuation. It earns its laugh on its own: the joke is
the word itself, the endless thumb-flick through bad news
at 2 a.m. that everybody recognises the moment they read
it. It says something true about the internet as a whole,
not one app or one site: the feed never ends, the news
never cheers up, and the reader never meant to stay this
long. It surprises by naming the reader's own behaviour
instead of the internet's content -- "cat videos" or
"arguments" would describe what is on it, while this
word describes what it does to you -- and it lands in
one beat, a word already in everyday use, spelled the
way everybody spells it.

LIMIT is 30 because the bounty gate allows UTF-8 text of
1 to 30 characters in /output/entry.txt. The validator
below guards the word against an edit that would push it
past the limit, split it into two words, or smuggle in
non-ASCII or control characters.
"""

import os

# The sealed word: the whole internet, named by what it
# does to you at 2 a.m.
ENTRY = "doomscrolling"

LIMIT = 30  # bounty gate: 1-30 characters, UTF-8 text


def _validate(text):
    """Accept only one clean word inside the character limit."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text:
        raise ValueError("entry must not be empty")
    if not text.isascii():
        # Character counts must mean the same thing everywhere,
        # so the word is plain ASCII only.
        raise ValueError("entry must be plain ASCII text")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if any(ch.isspace() for ch in text):
        # A single word has no spaces at all: a space would
        # turn it into a phrase, which loses to any one word.
        raise ValueError("entry must be a single word")
    if len(text) > LIMIT:
        raise ValueError(
            "entry is %d characters, past the %d limit" % (len(text), LIMIT)
        )
    if text.strip() != text:
        # Leading or trailing padding is dead weight the gate
        # still counts, so the word must start and end on a
        # letter.
        raise ValueError("entry must not pad itself with spaces")
    if not text.isprintable():
        raise ValueError("entry must contain no control characters")
    if not text.isalpha():
        # One word, letters only: no hyphen, no digit, no
        # punctuation hiding a second word inside it.
        raise ValueError("entry must be a single word")
    if not text.islower():
        # The word is spelled the way everybody spells it:
        # lower case, no capital doing extra work.
        raise ValueError("entry must be lower case")
    if len(text) < 3:
        # A one- or two-letter word cannot carry a joke
        # about the whole internet on its own.
        raise ValueError("entry is too short to describe the internet")
    return text


def main():
    entry = _validate(ENTRY)
    outdir = "/output" if os.path.isdir("/output") else "."
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(entry)
    print("%s (%d characters)" % (path, len(entry)))
    print(entry)


if __name__ == "__main__":
    main()
