from utilities.mongo_object import MongoObject
from jsonobject import JsonObject, StringProperty, IntegerProperty


class Foul(MongoObject, JsonObject):
    team_id = StringProperty()
    home_score = IntegerProperty()
    guest_score = IntegerProperty()

    type = StringProperty()
    player_number = IntegerProperty()
