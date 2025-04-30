#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 12:19:19 2023

@author: danielferreira
"""

# Import the data, you can find this tables on https://github.com/danielrferreira/pySTETV/tree/main/06%20-%20Utility%20%26%20References/Data/Processing%20Data/Baseball
folder = '../../06 - Utility & References/Data'
from os import chdir
chdir(folder)
import pandas as pd
# This one has the batting stats I am interested
batting_raw = pd.read_csv('batting_2021_2022_2023.csv')
# These 3 have team_ids for each player (and much more), but I am only interested in team_id
s2021 = pd.read_csv('swing_take_2021.csv')
s2022 = pd.read_csv('swing_take_2022.csv')
s2023 = pd.read_csv('swing_take_2023.csv')
sAll = pd.concat([s2021,s2022,s2023])

# Finding unique combination of team_ids, player_ids and year
unique_keys = sAll[['year','player_id', 'team_id']].drop_duplicates()
batting_w_team = batting_raw.merge(unique_keys,on=['year','player_id'],how='left') 

# Manually coded the teams, divisions and leagues
team_id = pd.Series([116,135,119,109,115,117,142,134,111,113,145,158,141,146,108,138,140,121,144,147,118,137,139,133,112,143,110,120,136,114])
team_name = pd.Series(['DET','SD','LAD','ARI','COL','HOU','MIN','PIT','BOS','CIN','CWS','MIL','TOR','MIA','LAA','STL','TEX','NYM','ATL','NYY','KC','SF','TB','OAK','CHC','PHI','BAL','WSH','SEA','CLE'])
division = pd.Series(['ALC','NLW','NLW','NLW','NLW','ALW','ALC','NLC','ALE','NLC','ALC','NLC','ALE','NLE','ALW','NLC','ALW','NLE','NLE','ALE','ALC','NLW','ALE','ALW','NLC','NLE','ALE','NLE','ALW','ALC'])
league = division.str[:2]
dim_team = pd.DataFrame({'team_id':team_id,'team_name':team_name,'division':division,'league':league})
dim_all = batting_w_team.merge(dim_team, on ='team_id',how='left')

# Some binary info I want to further test
dim_all['avg_220']=dim_all['batting_avg']>=0.22
dim_all['avg_240']=dim_all['batting_avg']>=0.240
dim_all['avg_260']=dim_all['batting_avg']>=0.260
dim_all['avg_280']=dim_all['batting_avg']>=0.280
dim_all['avg_300']=dim_all['batting_avg']>=0.3
dim_all['hr_10']=dim_all['home_run']>=10
dim_all['hr_20']=dim_all['home_run']>=20
dim_all['hr_30']=dim_all['home_run']>=30
dim_all['hr_40']=dim_all['home_run']>=40
dim_all['sb_05']=dim_all['r_total_stolen_base']>=5
dim_all['sb_10']=dim_all['r_total_stolen_base']>=10
dim_all['sb_15']=dim_all['r_total_stolen_base']>=15
dim_all['sb_20']=dim_all['r_total_stolen_base']>=20

# Keep the ones I want
dim_all = dim_all[['name', 'player_id', 'year', 'player_age', 'ab', 'pa', 'hit', 'single',
       'double', 'triple', 'home_run', 'strikeout', 'walk', 'k_percent',
       'bb_percent', 'batting_avg', 'slg_percent', 'on_base_percent',
       'on_base_plus_slg', 'b_rbi', 'r_total_caught_stealing',
       'r_total_stolen_base', 'exit_velocity_avg', 'sweet_spot_percent',
       'barrel_batted_rate', 'hp_to_1b', 'sprint_speed',
       'team_id', 'team_name', 'division', 'league',
        'avg_220','avg_240','avg_260','avg_280','avg_300','hr_10','hr_20','hr_30','hr_40','sb_05','sb_10','sb_15','sb_20']]

# Exporting to a CSV
dim_all.to_csv('player_batting_enriched.csv',index = False)

