import sys
from pathlib import Path

if len(sys.argv) != 2:
    print("Usage: python tally.py FILE", file=sys.stderr)
    raise SystemExit(2)

try:
    text = Path(sys.argv[1]).read_text(encoding="utf-8")
except (OSError, UnicodeError):
    print("Cannot read the file.", file=sys.stderr)
    raise SystemExit(1)

# ponytail: whitespace tokens; refine if punctuation-only input matters here.
print(len(text.split()))
