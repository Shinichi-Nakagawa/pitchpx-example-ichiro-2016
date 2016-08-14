#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import glob
import logging
import yaml
import pandas as pd
from pandas.io.common import EmptyDataError

__author__ = 'Shinichi Nakagawa'


class Csv2Pandas(object):
    """
    CSV to Pandas Datasets(MLBAM Datasets)
    """

    def __init__(self, setting_file='setting.yml'):
        """
        :param setting_file: settings yaml
        """
        self.setting = yaml.load(open('{}/{}'.format(os.path.abspath('.'), setting_file), 'r'))

    def create_game(self, prefix='mlbam_game_*.csv', table='game'):
        """
        create dataset for game
        :param prefix: filename pattern
        :param table: table name
        """
        self._create_datasets(prefix, table)

    def create_pitch(self, prefix='mlbam_pitch_*.csv', table='pitch'):
        """
        create dataset for pitch
        :param prefix: filename pattern
        :param table: table name
        """
        self._create_datasets(prefix, table)

    def create_atbat(self, prefix='mlbam_atbat_*.csv', table='atbat'):
        """
        create dataset for at bat
        :param prefix: filename pattern
        :param table: table name
        """
        self._create_datasets(prefix, table)

    def _create_datasets(self, prefix, table):
        """
        create dataset
        :param prefix: filename pattern
        :param table: table name
        """
        datasets = []
        for csv_dataset in glob.glob('{}/{}'.format(self.setting['config']['output'], prefix)):
            _, filename = os.path.split(csv_dataset)
            try:
                datasets.append(pd.read_csv(csv_dataset))
            except EmptyDataError as e:
                logging.warning('Empty Data:{}'.format(csv_dataset))
                continue
        dfs = pd.concat(datasets)
        dfs.to_csv('{}/{}.csv'.format(self.setting['dataset']['output'], table))


if __name__ == '__main__':
    c2b = Csv2Pandas()
    c2b.create_game()
    c2b.create_atbat()
    c2b.create_pitch()

