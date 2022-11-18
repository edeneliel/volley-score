from utilities.mongo_object import MongoObject
from jsonobject import JsonObject, IntegerProperty, StringProperty


class Substitution(MongoObject, JsonObject):
    team_id = StringProperty()
    home_score = IntegerProperty()
    guest_score = IntegerProperty()

    going_in = IntegerProperty()
    going_out = IntegerProperty()
