import json
import sys
from collections import Counter

def main():
    if len(sys.argv) < 2:
        print("Usage: python tools/top_programs.py path/to/map.json")
        sys.exit(1)

    path = sys.argv[1]
    with open(path, "r", encoding="utf-8") as f:
        call_map = json.load(f)

    counts = Counter()
    for caller, callees in call_map.items():
        for callee in callees:
            counts[callee] += 1

    print("Most-called programs:")
    for prog, count in counts.most_common(10):
        print(f"{prog}: {count} callers")

if __name__ == "__main__":
    main()
