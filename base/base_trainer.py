#!/usr/bin/env python
# coding=utf-8
# __author__='Alfred'

from utils.log import Logger


class BaseTrainer(object):
    def __init__(self, config, model, data_generator):
        self.cfg = config
        self.logger = Logger(self.cfg)
        self.model = model

    def train(self):
        pass

