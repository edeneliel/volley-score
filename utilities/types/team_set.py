from utilities.mongo_object import MongoObject
from jsonobject import IntegerProperty, JsonObject, ListProperty


class TeamSet(MongoObject, JsonObject):
    score = IntegerProperty(default=None)
    rotation = ListProperty(IntegerProperty())
