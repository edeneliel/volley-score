import typing
import strawberry


@strawberry.type
class GameType:
    id: str
    home_team_id: str
    guest_team_id: str

    home_team_players_ids: typing.List[str]
    guest_team_players_ids: typing.List[str]

    game_sets_ids: typing.List[str]

