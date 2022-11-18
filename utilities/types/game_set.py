import uuid
from utilities.types.serve import Serve
from utilities.types.team_set import TeamSet
from utilities.mongo_object import MongoObject
from jsonobject import ObjectProperty, ListProperty, JsonObject, StringProperty


class GameSet(MongoObject, JsonObject):
    __collection__ = 'game_sets'
    id = StringProperty(name='_id', default=str(uuid.uuid4()))

    game_id = StringProperty()
    home_team = ObjectProperty(TeamSet)
    guest_team = ObjectProperty(TeamSet)

    initial_receiver_team_id = StringProperty()
    serves = ListProperty(ObjectProperty(Serve))

    @property
    def game(self):
        from utilities.types.game import Game

        return Game.get(self.game_id)

    def _get_last_serve(self, team_id: str = None):
        if not team_id:
            return self.serves[-1]
        return next(reversed([serve for serve in self.serves if team_id == serve.team_id]), None)

    def give_point(self, team_id: str):
        game = self.game

        is_home_team = game.home_team_id == team_id
        team_set = self.home_team if is_home_team else self.guest_team

        last_serve = self._get_last_serve()

        if last_serve.team_id != team_id:
            team_set.score = team_set.score or 0

            last_team_serve = self._get_last_serve(team_id=team_id)
            current_player_index = team_set.rotation.index(last_team_serve.player_number) if last_team_serve else 0
            next_player_number = team_set.rotation[(current_player_index + 1) % len(team_set.rotation)]

            serve = Serve(team_id=team_id,
                          player_number=next_player_number,
                          home_score=self.home_team.score,
                          guest_score=self.guest_team.score)
            self.serves.append(serve)

        team_set.score += 1

        self.save()
