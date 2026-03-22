# ibmi-legacy-map
A simple tool that scans IBM i source ((RPG or CL code) and builds a simple map of which programs call which other programs as a first step for modernization assessments.

## Problem (Why this tool?)
Legacy IBM i applications often have thousands of programs. Understanding how they connect is the first step before any modernization work.
This project gives a lightweight way to:
- Get a quick picture of program-to-program calls.
- Spot central programs that many others depend on.
- Share a simple JSON map with architects, developers, and tooling.

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
