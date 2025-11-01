def fantasy_points(row):
    return (
        row['PTS']*1.0 +
        row['REB']*1.0 +
        row['AST']*2.0 +
        row['STL']*4.0 +
        row['BLK']*4.0 +
        row['TOV']*-2.0 +
        row['DD2']*2.0 +
        row['TD3']*3.0 +
        row['FGM']*2.0 +
        row['FGA']*-1.0 +
        row['FG3M']*1.0 +
        row['OREB']*1.0
    )