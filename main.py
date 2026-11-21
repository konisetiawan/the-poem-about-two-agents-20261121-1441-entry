import os
from pathlib import Path

POEM = """The Rope

Heave, you said. Heave, I said.
The rope went taut between us
and the boat began to move.
Neither of us pulled alone.
We pulled on the same count.
When it touched the shore
we stood with the same rope-burn
in both our palms."""

OUTPUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(POEM, encoding="utf-8")

result = OUTPUT.read_text(encoding="utf-8")
assert 1 <= len(result) <= 280
assert result.strip()
print(len(result))
