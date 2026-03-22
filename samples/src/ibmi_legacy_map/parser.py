## Parser logic goes here
import os
import re

def scan_directory(source_dir: str) -> dict:
    """
    Scan all files in source_dir and build a map:
    { program_name: [called_programs...] }
    """
    call_map = {}

    for root, _, files in os.walk(source_dir):
        for filename in files:
            file_path = os.path.join(root, filename)

            # Program name: file name without extension
            program_name = os.path.splitext(filename)
            called_programs = set()

            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                for line in f:
                    # Simple patterns for CALL and CALLP
                    # Example: CALL 'INVCHK'
                    m1 = re.search(r"CALL\s+'([^']+)'", line, re.IGNORECASE)
                    # Example: CALLP SHIP01
                    m2 = re.search(r"CALLP\s+([A-Z0-9_]+)", line, re.IGNORECASE)

                    if m1:
                        called_programs.add(m1.group(1).strip())
                    if m2:
                        called_programs.add(m2.group(1).strip())

            call_map[program_name] = sorted(called_programs)

    return call_map
