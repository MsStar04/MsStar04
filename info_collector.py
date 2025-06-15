"""Simple information collector agent.

This script reads text from one or more files, aggregates the content, and
prints the most common words. It's a minimal example of an 'AI agent'
collecting information from files.
"""

import argparse
from pathlib import Path
from collections import Counter


def collect_info(files):
    """Return the 10 most common words from the given files."""
    texts = []
    for file in files:
        texts.append(Path(file).read_text())
    combined = " ".join(texts)
    tokens = [word.strip(".,;!?:\"'()[]{}-").lower() for word in combined.split()]
    counts = Counter(filter(None, tokens))
    return counts.most_common(10)


def main():
    parser = argparse.ArgumentParser(description="Collect information from text files.")
    parser.add_argument("files", nargs="+", help="Paths to text files")
    args = parser.parse_args()
    for path in args.files:
        if not Path(path).is_file():
            parser.error(f"File not found: {path}")
    summary = collect_info(args.files)
    print("Top words:")
    for word, count in summary:
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
