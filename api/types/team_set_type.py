import typing
import strawberry


@strawberry.type
class TeamSetType:
    rotation: typing.List[int]
    score: typing.Optional[str]
