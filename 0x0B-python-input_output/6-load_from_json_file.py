#!/usr/bin/python3
import json


def load_from_json_file(filename):
    with open(filename, mode="w+", encoding="utf-8") as File:
        json.loads(filename)
