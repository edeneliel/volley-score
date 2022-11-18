import strawberry

from utilities.types.game import Game
from api.types.game_type import GameType


@strawberry.mutation
def start_game(
        self,
        home_team_id: str,
        guest_team_id: str,
) -> GameType:
    game = Game(home_team_id=home_team_id, guest_team_id=guest_team_id)
    return game

