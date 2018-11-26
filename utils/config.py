#!/usr/bin/env python
# coding=utf-8
# __author__='Alfred'

import json
from easydict import EasyDict


def get_config_from_json(json_file):
    with open(json_file, 'r') as config_file:
        config = json.load(config_file)

    return EasyDict(config)


def process_config(json_file):
    return get_config_from_json(json_file)
