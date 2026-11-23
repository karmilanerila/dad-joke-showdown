"""Dad Joke Showdown entry: one dad joke, written to /output/entry.txt."""

import os

JOKE = (
    "I told my router a joke at dinner, but it kept dropping the punchline "
    "-- I guess we just didn't have a strong connection."
)


def main() -> None:
    # Gate: entry must be 1-200 characters of real text, not only whitespace.
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, "joke must fit the 200-character gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
