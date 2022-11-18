import uuid
from typing import List
from utilities.types.serve import Serve
from utilities.types.game_set import GameSet
from utilities.mongo_object import MongoObject
from jsonobject import ListProperty, JsonObject, StringProperty


class Game(MongoObject, JsonObject):
    __collection__ = 'games'
    id = StringProperty(name='_id', default=str(uuid.uuid4()))

    home_team_id = StringProperty()
    guest_team_id = StringProperty()

    home_team_players_ids = ListProperty(StringProperty())
    guest_team_players_ids = ListProperty(StringProperty())

    game_sets_ids = ListProperty(StringProperty())

    def start_set(self, home_rotation: List[int], guest_rotation: List[int]):
        receiver_team = self.home_team_id  # TODO: Change it
        is_home = self.home_team_id == receiver_team

        game_set = GameSet(game_id=self.id, initial_receiver_team_id=receiver_team)
        game_set.home_team.rotation = home_rotation
        game_set.guest_team.rotation = guest_rotation

        team_set = game_set.home_team if is_home else game_set.guest_team
        serve = Serve(team_id=receiver_team,
                      player_number=team_set.rotation[0],
                      home_score=game_set.home_team.score,
                      guest_score=game_set.guest_team.score)

        game_set.serves.append(serve)

        self.game_sets_ids.append(game_set.id)
        self.save()
        return game_set.save()
