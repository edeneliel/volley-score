import strawberry

from utilities.types.game import Game
from api.types.game_type import GameType


@strawberry.mutation
def set_avalable_players(
        self,
        game_id: str,
        team_id: str,
        players_ids: str
) -> GameType:
    game = Game.get(game_id)
    try_teams = ['home', 'guest']
    return game

