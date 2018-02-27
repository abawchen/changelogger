import json


def read_patterns(filename):
    return json.load(open(filename))
