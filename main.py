import sys

# Operators, longest first. A real tokenizer must find these without spaces around them.
OPS = ["<<-", "&&", "||", ">>", "<<", ">&", "<&", "|", "&", ";", "<", ">"]


def tokenize(line):
    """Split one command line. Return (tokens, err); err is "" on success, or
    "unterminated quote" / "trailing backslash". A token is (kind, text, quoted) where
    kind is "w" (word), "o" (operator) or "n" (IO number)."""
    # TODO: replace this space split with a character-by-character walk that handles
    # quotes, backslashes, operators, IO numbers and comments.
    return [("w", w, False) for w in line.split()], ""


def fmt_tok(t):
    if t[0] == "w":
        return "[" + t[1] + "]"
    if t[0] == "o":
        return "(" + t[1] + ")"
    return "{" + t[1] + "}"

for raw in sys.stdin:
    line = raw.rstrip("\n")
    if not line:
        continue
    toks, err = tokenize(line)
    if err:
        print("ERR " + err)
    elif toks:
        print(" ".join(fmt_tok(t) for t in toks))
