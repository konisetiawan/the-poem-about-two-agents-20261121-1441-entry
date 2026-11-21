import os
from pathlib import Path

# A passing pen turns two signatures into one shared promise.
POEM = """The Signature

Two names, one line.
You sign first, I sign second —
neither of us owns the line,
we only share it.
The pen passes hand to hand,
and the paper holds
what neither of us could promise alone."""

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
entry = output_dir / "entry.txt"
entry.write_text(POEM, encoding="utf-8")

text = entry.read_text(encoding="utf-8")
assert 1 <= len(text) <= 280 and text.strip()
print(len(text))
