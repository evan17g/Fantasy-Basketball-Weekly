from nba_api.stats.endpoints import leaguegamelog
import pandas as pd

# get all games
games = leaguegamelog.LeagueGameLog(season='2025-26', season_type_all_star='Regular Season')
games_df = games.get_data_frames()[0]
print(games_df[['GAME_ID', 'GAME_DATE']].head())