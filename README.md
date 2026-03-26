# ibmi-legacy-map
A simple tool that scans IBM i source ((RPG or CL code) and builds a simple map of which programs call which other programs as a first step for modernization assessments.

## What ibmi-legacy-map does (v0.1)
For the first version, the tool focuses on:
- Read source files from a folder (for example, RPG or CL members exported to the file system).
- Look for simple call statements (like `CALL` or `CALLP`).
- Produce a JSON file that maps each program to the list of programs it calls.

## Quick test (local)
Once you clone the repository on your machine:

```bash
python -m ibmi_legacy_map ./samples/src ./output/map.json
```

This will scan the sample files and create `./output/map.json` with a simple call map.

## Why this matters

Legacy IBM i applications often have many programs, and it is hard to see how they are connected.
Before any modernization work, teams need a quick view of:

- Which programs call which other programs.
- Which parts of the system are most central and risky to touch.

`ibmi-legacy-map` gives a lightweight, scriptable way to see these relationships in one place.
The JSON output can be used as a starting point for architecture reviews, API planning, and impact analysis.


## Example: using it on a real codebase

1. Export your RPG/CL source members from IBM i to a folder (for example, using CPYTOSTMF or similar).
2. Run `ibmi-legacy-map` on that folder to produce a JSON file.
3. Open the JSON to:
   - Find heavily used programs (called by many others).
   - Decide which programs to wrap as APIs first.
   - See which areas of the system will be touched by a change.

## Helper: find the most-called programs

After you generate `map.json`, you can run:

```bash
python tools/top_programs.py output/map.json
```

This prints the programs that are called most often.
These are usually good candidates to review carefully or to wrap behind stable APIs before you change them.
