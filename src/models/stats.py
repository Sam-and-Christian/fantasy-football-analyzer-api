class PlayerStats():
    def __init__(self, season, game, date, team, away, opp):
        self._season = season
        self._game = game
        self._date = date
        self._team = team
        self._away = away
        self._opp = opp

    def __str__(self) -> str:
        return {
        'season': self._season,
        'game': self._game,
        'date': self._date,
        'team': self._team,
        'away': self._away,
        'opponent': self._opp
    }