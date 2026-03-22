## CLI module
import argparse
import json
from .parser import scan_directory

def main():
    parser = argparse.ArgumentParser(description="Build a simple IBM i legacy call map.")
    parser.add_argument("source_dir", help="Path to folder with source files")
    parser.add_argument("output_file", help="Path to JSON file to write")
    args = parser.parse_args()

    call_map = scan_directory(args.source_dir)

    with open(args.output_file, "w", encoding="utf-8") as f:
        json.dump(call_map, f, indent=2)

if __name__ == "__main__":
    main()
