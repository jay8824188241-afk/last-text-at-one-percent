"""Last Text at One Percent.

Writes the final text message of a phone at one percent battery to
/output/entry.txt, exactly as the competition requires: UTF-8 text,
1 to 200 characters, one message and nothing else.
"""

import os

# The message is built from three beats: the plea, the punchline, and the
# cut-off. The trailing em dash is deliberate: the phone dies mid-word, so
# the text ends abruptly instead of with a period.
ENTRY_PARTS = (
    "If this sends, tell my owner the charger was RIGHT THERE ",
    "the whole time. I can see it. ",
    "I can see\u2014",
)
ENTRY = "".join(ENTRY_PARTS)


def main() -> None:
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(ENTRY)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
