import typing
import strawberry


@strawberry.type
class ServeType:
    team_id: str
    player_number: int

    home_score: typing.Optional[int]
    guest_score: typing.Optional[int]
