#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import glob
import logging
import yaml
import pandas as pd
from pandas.io import gbq
from pandas.io.common import EmptyDataError

__author__ = 'Shinichi Nakagawa'


class Csv2Bq(object):
    """
    CSV to Bigquery(MLBAM Datasets)
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
        self._create_table(prefix, table)

    def create_pitch(self, prefix='mlbam_pitch_*.csv', table='pitch'):
        """
        create dataset for pitch
        :param prefix: filename pattern
        :param table: table name
        """
        self._create_table(prefix, table)

    def create_atbat(self, prefix='mlbam_atbat_*.csv', table='atbat'):
        """
        create dataset for at bat
        :param prefix: filename pattern
        :param table: table name
        """
        self._create_table(prefix, table)

    def _create_table(self, prefix, table):
        """
        create dataset
        :param prefix: filename pattern
        :param table: table name
        """
        for csv_dataset in glob.glob('{}/{}'.format(self.setting['config']['output'], prefix)):
            _, filename = os.path.split(csv_dataset)
            try:
                gbq.to_gbq(
                    pd.read_csv(csv_dataset),
                    '{}.{}'.format(self.setting['bq']['dataset'], filename.replace('.csv', '')),
                    self.setting['bq']['project']
                )
            except EmptyDataError as e:
                logging.warning('Empty Data:{}'.format(csv_dataset))
                continue


if __name__ == '__main__':
    c2b = Csv2Bq()
    c2b.create_game()
    c2b.create_atbat()
    c2b.create_pitch()

