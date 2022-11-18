import typing
import strawberry


@strawberry.type
class TeamType:
    id: str
    name: str
    players_ids: typing.List[str]
