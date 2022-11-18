import typing
import strawberry

from api.types.team import TeamType
from utilities.types.game import Game
from utilities.types.team import Team
from api.types.game_type import GameType
from api.types.player_type import PlayerType
from api.types.league_type import LeagueType
from utilities.types.game_set import GameSet
from api.types.game_set_type import GameSetType
from api.queries.get_association_data import get_all_leagues, get_all_teams, get_all_players


def get_filters(**kwargs):
    return {
        key: value
        for key, value
        in kwargs.items()
        if value
    }


def get_games(id: typing.Optional[str] = None):
    filters = get_filters(id=id)
    return Game.find(**filters)


def get_teams(id: typing.Optional[str] = None):
    filters = get_filters(id=id)
    return Team.find(**filters)


def get_game_sets(id: typing.Optional[str] = None):
    filters = get_filters(id=id)
    return GameSet.find(**filters)


@strawberry.type
class Query:
    games: typing.List[GameType] = strawberry.field(resolver=get_games)
    teams: typing.List[TeamType] = strawberry.field(resolver=get_teams)
    games_sets: typing.List[GameSetType] = strawberry.field(resolver=get_game_sets)

    all_teams: typing.List[TeamType] = strawberry.field(resolver=get_all_teams)
    all_players: typing.List[PlayerType] = strawberry.field(resolver=get_all_players)
    all_leagues: typing.List[LeagueType] = strawberry.field(resolver=get_all_leagues)
