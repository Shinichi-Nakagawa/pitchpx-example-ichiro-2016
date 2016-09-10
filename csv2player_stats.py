#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

__author__ = 'Shinichi Nakagawa'

INPUT_DIR = '~/Google ドライブ/mlbam/{}'
OUTPUT_DIR= './output/player_stats'

PLAYERS = (
    # {'bat_box_name': 'Suzuki, I', 'file_name': 'ichiro_suzuki_{year}_{dataset}.csv'},
    # {'bat_box_name': 'Votto', 'file_name': 'joey_votto_{year}_{dataset}.csv'},
    {'pit_box_name' :'Darvish', 'file_name': 'yu_darvish_{year}_{dataset}.csv'},
)


def create_batter_stats(input_path, year, dataset):
    df = pd.read_csv('/'.join([input_path, '{}{}.csv'.format(dataset, year)]))
    for player in PLAYERS:
        # df_stats = df.query("bat_box_name=='{bat_box_name}' and regseason_fl == 'T'".format(**player))
        df_stats = df.query("pit_box_name=='{pit_box_name}' and regseason_fl == 'T'".format(**player))
        df_stats.to_csv('/'.join([OUTPUT_DIR, player['file_name'].format(year=year, dataset=dataset)]))


if __name__ == '__main__':

    for year in range(2013, 2017):
        create_batter_stats(INPUT_DIR.format(year), year, 'atbat')
        create_batter_stats(INPUT_DIR.format(year), year, 'pitch')