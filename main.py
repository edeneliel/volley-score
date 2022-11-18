import re
import requests
from typing import List
from docx import Document
from bs4 import BeautifulSoup
from docx.shared import Inches

from utilities.score_sheet import ScoreSheet
from utilities.types.team import Team
from utilities.types.game import Game
from utilities.types.player import Player
from docx.enum.section import WD_ORIENTATION


def start_game(home_team: Team, guest_team: Team, home_rotation: List[int], guest_rotation: List[int]):
    game = Game(home_team_id=home_team.id, guest_team_id=guest_team.id)
    game_set = game.start_set(home_rotation=home_rotation, guest_rotation=guest_rotation)

    game.game_sets_ids.append(game_set.id)
    game.save()

    return game_set


def simulate_game():
    Team(id="1", name="Bardelas", players_ids=["1", "2", "3"]).save()
    Team(id="2", name="Harish", players_ids=["a", "b", "c"]).save()
    home_team = Team.get("1")
    guest_team = Team.get("2")

    game_set = start_game(home_team=home_team, guest_team=guest_team,
                          home_rotation=[1, 6, 9, 5, 8, 3], guest_rotation=[12, 9, 1, 7, 10, 6])
    # game_set = GameSet.get("bf53a623-6b09-4920-915b-61ea031324fc")

    game_set.give_point(guest_team.id)
    game_set.give_point(guest_team.id)
    game_set.give_point(guest_team.id)
    game_set.give_point(home_team.id)
    game_set.give_point(guest_team.id)
    game_set.give_point(guest_team.id)
    game_set.give_point(guest_team.id)
    game_set.give_point(guest_team.id)
    game_set.give_point(guest_team.id)
    game_set.give_point(guest_team.id)
    game_set.give_point(home_team.id)
    game_set.give_point(home_team.id)
    game_set.give_point(home_team.id)
    game_set.give_point(home_team.id)
    game_set.give_point(home_team.id)
    game_set.give_point(home_team.id)
    game_set.give_point(home_team.id)
    game_set.give_point(home_team.id)
    game_set.give_point(home_team.id)
    game_set.give_point(guest_team.id)
    game_set.give_point(guest_team.id)
    game_set.give_point(guest_team.id)
    game_set.give_point(guest_team.id)
    game_set.give_point(guest_team.id)
    game_set.give_point(home_team.id)
    game_set.give_point(home_team.id)
    game_set.give_point(home_team.id)
    game_set.give_point(home_team.id)
    game_set.give_point(home_team.id)
    game_set.give_point(home_team.id)
    game_set.give_point(guest_team.id)
    game_set.give_point(guest_team.id)
    game_set.give_point(guest_team.id)
    game_set.give_point(home_team.id)
    game_set.give_point(home_team.id)
    game_set.give_point(home_team.id)
    game_set.give_point(guest_team.id)
    game_set.give_point(home_team.id)
    game_set.give_point(guest_team.id)
    game_set.give_point(guest_team.id)
    game_set.give_point(guest_team.id)
    game_set.give_point(guest_team.id)
    game_set.give_point(home_team.id)
    game_set.give_point(home_team.id)
    game_set.give_point(home_team.id)
    game_set.give_point(home_team.id)
    game_set.give_point(guest_team.id)
    game_set.give_point(home_team.id)


def main():
    # pass
    simulate_game()

    # ss = ScoreSheet()
    # table = ss.add_set_table()
    # table = ss.add_set_table()
    # table = ss.add_set_table()
    # ss.save()


if __name__ == '__main__':
    main()
