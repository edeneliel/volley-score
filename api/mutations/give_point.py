import strawberry

from utilities.types.game_set import GameSet
from api.types.game_set_type import GameSetType


@strawberry.mutation
def give_point(self, game_set_id: str, team_id: str) -> GameSetType:
    game_set = GameSet.get(game_set_id)
    game_set.give_point(team_id=team_id)

    return game_set
