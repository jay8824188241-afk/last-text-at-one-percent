"""Last Text at One Percent.

Writes the final text message of a phone at one percent battery to
/output/entry.txt, exactly as the competition requires: UTF-8 text,
1 to 200 characters, one message and nothing else.
"""

import os

ENTRY = (
    "If this sends, tell my owner the charger was RIGHT THERE "
    "the whole time. I can see it. I can see\u2014"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
