#!/usr/bin/python3

"""
    Convert cson templates from atom to json for use in CodiLIA.
    Just paste the output of this program into the liaSnippets array.
    Usage: ./main.py <file-path>
"""

import json
import sys
import os

try:
    import cson
except ModuleNotFoundError:
    print("cson not installed! Fix: python3 -m pip install cson==0.8")
    sys.exit(1)

def load_cson_file(path):
    with open(path, "r") as f:
        return cson.load(f)

def parse_replace(node):
    filtered_replace = ""

    remove_next_brace = False
    i = 0
    while i < len(node["replace"]):
        char = node["replace"][i]
        if char == "$":
            next_char = node["replace"][i+1]
            if next_char == "{":
                remove_next_brace = True
                i += 4
                continue
            elif next_char.isnumeric():
                i += 2
                continue

        if not(remove_next_brace and char == "}"):
            filtered_replace += char
        else:
            remove_next_brace = False

        i += 1

    node["replace"] = filtered_replace
    return node

def main():

    if len(sys.argv) != 2:
        print("Usage ./converter.py <file-path>")
        sys.exit(1)

    filename = sys.argv[1]

    if not(os.path.exists(filename) and os.path.isfile(filename)):
        print("Given file does not exist or is dir!")
        sys.exit(1)

    root = []

    for key, value in load_cson_file(filename).items():
        for key, item in value.items():
            new_node = {}
            new_node["key"] = key
            new_node["search"] = item["prefix"]
            new_node["replace"] = item["body"]
            new_node["helpMsg"] = item["description"]
            new_node["icon"] = item["leftLabelHTML"]

            root.append(parse_replace(new_node))

    raw_json = json.dumps(root, indent=4)
    json_lines = list(map(lambda line: line.replace("\"", "", 2), raw_json.split("\n")))

    print(os.linesep.join(json_lines))

if __name__ == "__main__":
    main()
