"""Check a translation PR against the files on its base branch."""
import argparse
import json
import re
import subprocess
from collections import Counter
from pathlib import PurePosixPath

TOKENS = re.compile(
    r"%%|%arg|\$\{[^}]+\}|\\\([^)]*\)|"
    r"%(?:(?P<index>\d+)\$)?(?P<spec>#@\w+@|"
    r"[-+0#']*\d*(?:\.\d+)?(?:hh|ll|[hlLqztj])?[@diuoxXfFeEgGaAcCsSp])"
)
MARKUP = re.compile(r"\n|\*\*|\x60|(?:https?|dockflow)://[A-Za-z0-9_./?&=%:+#~-]+")


def signature(text):
    counts = Counter(MARKUP.findall(text))
    implicit = 0
    modes = set()
    for match in TOKENS.finditer(text):
        if match["spec"] is None:
            counts[match[0]] += 1
            continue
        index = match["index"]
        modes.add("explicit" if index else "implicit")
        if not index:
            implicit += 1
        counts[int(index) if index else implicit, match["spec"]] += 1
    if len(modes) > 1:
        raise ValueError("mixed positional and implicit format arguments")
    return counts


def unique(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate key {key!r}")
        result[key] = value
    return result


def git(*args):
    return subprocess.check_output(["git", *args])


def check(before, after, location):
    if before == after:
        return
    if isinstance(before, dict):
        if not isinstance(after, dict) or before.keys() != after.keys():
            raise ValueError(f"{location}: keys or plural forms changed")
        for key in before:
            check(before[key], after[key], f"{location} / {key}")
        return
    if not isinstance(after, str) or not after.strip():
        raise ValueError(f"{location}: enter a nonempty translation")
    if signature(before) != signature(after):
        raise ValueError(f"{location}: placeholders, links, or formatting changed")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("base")
    parser.add_argument("head")
    args = parser.parse_args()
    changed = git("diff", "--name-only", "-z", args.base, args.head, "--", "translations")
    for filename in changed.decode().split("\0"):
        if not filename:
            continue
        path = PurePosixPath(filename)
        if len(path.parts) != 3 or path.parts[1] == "en" or path.suffix != ".json":
            raise ValueError(f"{filename}: suggest English or structural changes in an issue")
        snapshots = [json.loads(git("show", f"{rev}:{filename}"), object_pairs_hook=unique)
                     for rev in (args.base, args.head)]
        check(*snapshots, filename)
        print(f"Checked {filename}")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, subprocess.CalledProcessError) as error:
        raise SystemExit(str(error))

