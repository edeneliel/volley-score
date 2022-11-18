from utilities.mongo_object import MongoObject
from jsonobject import IntegerProperty, StringProperty, JsonObject


class Serve(MongoObject, JsonObject):
    team_id = StringProperty()
    home_score = IntegerProperty()
    guest_score = IntegerProperty()
    player_number = IntegerProperty()
