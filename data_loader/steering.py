#!/usr/bin/env python
# coding=utf-8
# __author__='Alfred'

import csv
import os
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle


class SteeringDataLoader(object):
    def __init__(self, config):
        self.cfg = config
        self.train_set = []
        self.test_set = []

        self._load_data()

    def _load_data(self):
        fp = self.cfg.file_path
        test_size = self.cfg.get('test_percentage', .2)
        data = []
        with open(fp, 'r') as f:
            csv_reader = csv.reader(f)
            # skip header
            next(csv_reader)
            for line in csv_reader:
                frame_id = line[4]
                fp = os.path.join(fp, line[5])
                angle = line[6]

                # filter out center images
                if frame_id == 'center_camera':
                    data.append((fp, angle))

        # split data into train & test sets
        self.train_set, self.test_set = train_test_split(data, test_size=test_size)

    def next_batch(self, samples):
        batch_size = self.cfg.get('batch_size', 64)
        n_samples = len(samples)
        while 1:
            samples = shuffle(samples)
            for sid in range(0, n_samples, batch_size):
                batch = samples[sid: sid+batch_size]
                images = [plt.imread(it[0]) for it in batch]
                angles = [np.float32(it[1]) for it in batch]

                yield np.array(images), np.array(angles)

    @property
    def train_generator(self):
        return self.next_batch(self.train_set)

    @property
    def test_generator(self):
        return self.next_batch(self.test_set)

    @property
    def train_size(self):
        return len(self.train_set)
