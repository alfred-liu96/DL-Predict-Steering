#!/usr/bin/env python
# coding=utf-8
# __author__='Alfred'

from utils.log import Logger


class BaseModel(object):
    def __init__(self, config):
        self.cfg = config
        self.logger = Logger(self.cfg)

        self._model = None
        self._build_model()

    def _build_model(self):
        raise NotImplementedError

    def save(self):
        self.logger.msg('Saving model...')
        sp = self.cfg.save_path
        self._model.save(sp)
        self.logger.msg('Model saved')

    @property
    def model(self):
        return self._model
