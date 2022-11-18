import re
import typing
import requests
from bs4 import BeautifulSoup

from api.types.player_type import PlayerType
from api.types.team import TeamType
from utilities.config import Constants
from api.types.league_type import LeagueType


def get_all_leagues(year: int) -> typing.List[LeagueType]:
    leagues = []
    response = requests.get(f'{Constants.VOLLEYBALL_ASSOCIATION_URL}boards.asp?cYear={year}&TypeId=0')
    board_items = BeautifulSoup(response.content, features="html.parser").find_all(class_="board")

    for board_item in board_items:
        a_object = board_item.a
        league_id = re.search('.*?LeagueId=(.*?)&.*', a_object.get('href')).group(1)

        leagues.append(LeagueType(id=int(league_id), name=a_object.text))

    return leagues


def get_all_teams(league_id: str, year: int) -> typing.List[TeamType]:
    teams = []
    response = requests.get(f'{Constants.VOLLEYBALL_ASSOCIATION_URL}league.asp?LeagueId={league_id}&cYear={year}')
    a_objects = BeautifulSoup(response.content, features="html.parser").find(class_="legue-table").find_all('a')
    for a_object in a_objects:
        href = a_object.get('href')
        if not href.startswith('team'):
            continue

        team_id = re.search('.*?TeamId=(.*?)&.*', href).group(1)
        team_name = re.search('.*?\\. *(.*)', a_object.text).group(1)

        teams.append(TeamType(id=team_id, name=team_name, players_ids=[]))

    return teams


def get_all_players(team_id: str, year: int) -> typing.List[PlayerType]:
    players = []
    response = requests.get(f'{Constants.VOLLEYBALL_ASSOCIATION_URL}team.asp?TeamId={team_id}&cYear={year}')
    players_response = BeautifulSoup(response.content, features="html.parser").find_all(class_="player")
    for player in players_response:
        player_details = player.find(class_='player-details')
        picture = player.img.get('src')
        if picture.startswith('/'):
            picture = Constants.VOLLEYBALL_ASSOCIATION_URL + picture

        player_name = player_details.find_next(class_='name').text
        player_number = int(re.sub('\\D', '', player_details.find_next(class_='number').text))

        players.append(PlayerType(
            id=f'{player_name}~{player_number}',
            name=player_name,
            number=player_number,
            picture=picture)
       )

    return players

