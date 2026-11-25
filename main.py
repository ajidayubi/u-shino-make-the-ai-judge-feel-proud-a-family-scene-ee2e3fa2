"""Make the AI Judge Feel Proud: A Family Scene.

Writes one short family scene (one or two lines, at most 280 characters)
to /output/entry.txt, where the sealed gate scorer reads it.

The scene: a boy builds a crooked birdhouse for a week; when the first
sparrow moves in, his quiet, wry whisper to his dad turns a lopsided
little project into the proudest moment of the summer. Warm, heartfelt,
funny in a small recognisable way, and specific down to the lean.
"""

import os
import sys

SCENE = (
    "My son spent a week building a birdhouse that leans a little to the "
    "left, and when the first sparrow moved in he whispered, 'See, Dad? "
    "Somebody finally likes my work.' I have never been prouder of a "
    "crooked roof."
)


def main() -> int:
    text = SCENE
    # Gate: UTF-8 text of 1 to 280 characters, not only white space.
    if not (1 <= len(text) <= 280):
        print(f"scene is {len(text)} characters, must be 1-280", file=sys.stderr)
        return 1
    if not text.strip():
        print("scene is blank", file=sys.stderr)
        return 1
    if text.count("\n") > 1:
        print("scene must be one or two lines", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(text)
    print(f"chars: {len(text)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
