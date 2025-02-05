import pandas as pd
import numpy as np

df = pd.read_csv('C:/Users/desir/Downloads/players_stats_by_season_full_details.csv')

fgm = df['FGM'].to_numpy()
fga = df['FGA'].to_numpy()
tpm = df['3PM'].to_numpy()
tpa = df['3PA'].to_numpy()
ftm = df['FTM'].to_numpy()
fta = df['FTA'].to_numpy()
pts = df['PTS'].to_numpy()
min_played = df['MIN'].to_numpy()
blk = df['BLK'].to_numpy()
stl = df['STL'].to_numpy()

field_goal_accuracy = np.divide(fgm, fga, where=fga!=0)  
three_point_accuracy = np.divide(tpm, tpa, where=tpa!=0)
free_throw_accuracy = np.divide(ftm, fta, where=fta!=0)
average_points_per_minute = np.divide(pts, min_played, where=min_played!=0)
average_blocks_per_game = blk  
average_steals_per_game = stl  

df['Field Goal Accuracy'] = field_goal_accuracy
df['Three Point Accuracy'] = three_point_accuracy
df['Free Throw Accuracy'] = free_throw_accuracy
df['Average Points per Minute'] = average_points_per_minute
df['Average Blocks per Game'] = average_blocks_per_game
df['Average Steals per Game'] = average_steals_per_game

numeric_cols = ['Field Goal Accuracy', 'Three Point Accuracy', 'Free Throw Accuracy', 
                'Average Points per Minute', 'Average Blocks per Game', 'Average Steals per Game']

grouped = df.groupby(['Player', 'Season'])[numeric_cols]
season_stats = grouped.mean().reset_index()

print(season_stats.head()) 