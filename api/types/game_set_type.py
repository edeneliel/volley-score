import typing
import strawberry
from api.types.serve_type import ServeType
from api.types.team_set_type import TeamSetType


@strawberry.type
class GameSetType:
    id: str
    game_id: str
    home_team: TeamSetType
    guest_team: TeamSetType
    initial_receiver_team_id: str
    serves: typing.List[ServeType]
