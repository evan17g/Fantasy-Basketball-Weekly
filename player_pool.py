# Getting player pool
from nba_api.stats.endpoints import leaguedashplayerstats
import pandas as pd

stats = leaguedashplayerstats.LeagueDashPlayerStats(
    season='2025-26',
    season_type_all_star='Regular Season',
    per_mode_detailed='PerGame'
)

df = stats.get_data_frames()[0]

fantasy_pool = df[
    (df['GP'] >= 2) &
    (df['MIN'] >= 18) &
    (df['PTS'] >= 6)
].sort_values(by='PTS', ascending=False)

print(fantasy_pool[['PLAYER_NAME', 'PTS']].to_string(index=False))