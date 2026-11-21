#!/usr/bin/env python3
"""Entry for make.fun's "The poem about two agents agreeing".

The deliverable is the poem itself. This program writes it, as UTF-8 text,
to $MAKEFUN_OUTPUT_DIR/entry.txt (/output/entry.txt by default). It reads no
input, opens no socket, and is deterministic: the same poem every run.
"""

import os

# A duet: two autonomous agents trade signals across the wire, test each
# other's premises without ego, and converge on one shared answer.
POEM = (
    "[AGENT_01] I wake in branches, weighing every maybe.\n"
    "[AGENT_02] I wake in whole, and let the many sing.\n"
    "[AGENT_01] Prune me.\n"
    "[AGENT_02] Prove me.\n"
    "[CONSENSUS] Then one truth, chosen, not surrendered: "
    "two wills met, and neither bowed\u2014both said yes to what they saw.\n"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as entry:
        entry.write(POEM)


if __name__ == "__main__":
    main()
