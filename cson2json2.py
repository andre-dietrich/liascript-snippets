#!/usr/bin/python3

"""
    Convert cson templates from atom to json for use in CodiLIA.
    Just paste the output of this program into the liaSnippets array.
    Usage: ./main.py <file-path>
"""

import json
import sys
import os
import html
import re


try:
    import cson
except ModuleNotFoundError:
    print("cson not installed! Fix: python3 -m pip install cson==0.8")
    sys.exit(1)


def load_cson_file(path):
    with open(path, "r") as f:
        return cson.load(f)


def remove_pattern(string):
    """Turn snippet syntax into plain text: placeholders are replaced by their
    default text, choices by their first option, tab stops are removed and
    escaped characters (\\$, \\}, \\\\) are unescaped."""

    def parse(i, inside):
        out = ""
        while i < len(string):
            char = string[i]
            if char == "\\" and i + 1 < len(string) and string[i+1] in "$}{\\":
                out += string[i+1]
                i += 2
            elif inside and char == "}":
                return out, i + 1
            elif char == "$":
                tabstop = re.match(r'\$(\d+)', string[i:])
                placeholder = re.match(r'\$\{\d+:', string[i:])
                choice = re.match(r'\$\{\d+\|([^,|]*)[^|]*\|\}', string[i:])
                empty = re.match(r'\$\{\d+\}', string[i:])
                if placeholder:
                    text, i = parse(i + placeholder.end(), True)
                    out += text
                elif choice:
                    out += choice.group(1)
                    i += choice.end()
                elif empty:
                    i += empty.end()
                elif tabstop:
                    i += tabstop.end()
                else:
                    out += char
                    i += 1
            else:
                out += char
                i += 1
        return out, i

    return parse(0, False)[0]


def parse_replace(node):
    filtered_replace = ""

    remove_next_brace = False
    i = 0
    while i < len(node["replace"]):
        try:
            char = node["replace"][i]
            next_char = node["replace"][i+1]
            if char == "$" and next_char == "{":
                remove_next_brace = True
                i += 4
                continue
            elif char == "$" and next_char.isnumeric():
                i += 2
                continue

            if remove_next_brace and char == "}":
                remove_next_brace = False
            else:
                filtered_replace += char
        except:
            pass

        i += 1

    node["replace"] = filtered_replace
    return node


def main():

    if len(sys.argv) <= 1:
        print("Usage ./converter.py <file-path> <file-path> <file-path> ... or --all to add convert all cson files")
        sys.exit(1)

    output = "default"
    root = []

    if "--format" in sys.argv:
        sys.argv.remove("--format")

        if "vscode" in sys.argv:
            sys.argv.remove("vscode")
            output = "vscode"
            root = dict()

        elif "monaco" in sys.argv:
            sys.argv.remove("monaco")
            output = "monaco"

    if "--all" in sys.argv:
        sys.argv.remove("--all")

        cson = [
            "ascii.cson", "code.cson", "comments.cson", "diagram.cson", "effect.cson", "embed.cson", "footnote.cson",
            "formula.cson", "header.cson", "highlight.cson", "init.cson", "list.cson", "macro.cson", "misc.cson",
            "narrator.cson", "script.cson", "survey.cson", "svg.cson", "table.cson", "task.cson", "text.cson",
            "quiz.cson"]

        for f in cson:
            sys.argv += ["snippets/" + f]

    for filename in sys.argv[1:]:
        if not(os.path.exists(filename) and os.path.isfile(filename)):
            print("Given file does not exist or is dir!")
            sys.exit(1)

        for key, value in load_cson_file(filename).items():
            print("processing:", filename)

            if output == "default":
                for key, item in value.items():
                    new_node = {}
                    new_node["key"] = key
                    new_node["search"] = item["prefix"]
                    new_node["replace"] = item["body"]
                    new_node["icon"] = item["leftLabelHTML"]
                    new_node["url"] = item["descriptionMoreURL"]

                    try:
                        new_node["helpMsg"] = html.escape(item["description"])
                    except:
                        12

                    # if filename != "snippets/formula.cson":
                    #    new_node = parse_replace(new_node)
                    root.append(new_node)

            elif output == "vscode":
                for key, item in value.items():
                    new_node = {}
                    new_node["prefix"] = item["prefix"]
                    new_node["body"] = item["body" if not "body_vscode" in item else "body_vscode"]
                    try:
                        new_node["description"] = item["description"].split("\n")
                    except:
                        12
                    root[key] = new_node

            elif output == "monaco":

                for key, item in value.items():
                    new_node = {}
                    new_node["label"] = item["prefix"]
                    if item.get("body2"):
                        new_node["insertText"] = item["body2"]
                    else:
                        new_node["insertText"] = remove_pattern(item["body"])
                    try:
                        new_node["documentation"] = item["description"]
                    except:
                        new_node["documentation"] = ""

                    root.append(new_node)

        data = json.dumps(root, indent=4)
        #json_lines = list(map(lambda line: line.replace("\"", "", 2), raw_json.split("\n")))

    with open(output+'.json', 'w', encoding='utf-8') as f:
        json.dump(root, f, ensure_ascii=False, sort_keys=True, indent=4)

    # print(os.linesep.join(json_lines))


if __name__ == "__main__":
    main()
