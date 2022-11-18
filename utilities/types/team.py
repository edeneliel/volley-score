from utilities.mongo_object import MongoObject
from jsonobject import StringProperty, JsonObject, ListProperty


class Team(MongoObject, JsonObject):
    __collection__ = 'teams'
    id = StringProperty(name='_id')

    name = StringProperty()
    players_ids = ListProperty(StringProperty())
