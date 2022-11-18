from utilities.mongo_object import MongoObject
from jsonobject import StringProperty, IntegerProperty, JsonObject


class Player(MongoObject, JsonObject):
    __collection__ = 'players'

    name = StringProperty()
    picture = StringProperty()
    number = IntegerProperty()
