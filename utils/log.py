#!/usr/bin/env python
# coding=utf-8
# __author__='Alfred'

import logging

DEBUG = logging.DEBUG
INFO = logging.INFO
WARNING = logging.WARNING
ERROR = logging.ERROR
CRITICAL = logging.CRITICAL

level_names = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL,
}


class Logger(object):
    def __init__(self, config):
        self._logger = logging.getLogger(__name__)
        logging.basicConfig(
            level=level_names[config.log_level],
            format='%(asctime)s %(levelname)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S')

    def msg(self, message=None, _level=logging.INFO, **kw):
        level = kw.pop('level', _level)
        message = kw.pop('format', message)
        self._logger.log(level, message, *[kw] if kw else [])

    def err(self, message):
        self._logger.exception(message)
