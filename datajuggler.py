#!/usr/bin/env python3
"""
Data Juggler; convert stdin to/from different formats liks JSON, YAML, CSV, TSV
"""

from sys import stdin, argv
from os.path import basename

import json, yaml, csv

loaders = {
    "j": json.load,
    "y": lambda x: yaml.load(x, Loader=yaml.SafeLoader),
    "t": lambda x: list(csv.DictReader(x, delimiter="\t")),
    "c": lambda x: list(csv.DictReader(x)),
}

dumpers = {
    "j": lambda x: json.dumps(x, indent=4),
    "y": yaml.dump,
}

if __name__ == "__main__":
    l, d = basename(argv[0])
    loader = loaders[l]
    dumper = dumpers[d]

    print(dumper(loader(stdin)))
