#!/usr/bin/env python
# coding=utf-8
# __author__='Alfred'

from utils.config import process_config
from data_loader.steering import SteeringDataLoader


def main():
    config = process_config('configs/steering.json')

    data_loader = SteeringDataLoader(config)


if __name__ == '__main__':
    main()
