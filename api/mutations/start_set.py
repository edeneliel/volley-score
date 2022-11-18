import typing

import strawberry

from utilities.types.game import Game
from api.types.game_set_type import GameSetType


@strawberry.mutation
def start_set(
        self,
        game_id: str,
        home_rotation: typing.List[int],
        guest_rotation: typing.List[int]
) -> GameSetType:
    game = Game.get(game_id)
    game_set = game.start_set(home_rotation=home_rotation, guest_rotation=guest_rotation)

    return game_set
