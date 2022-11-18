from connectors.mongo_connect import MongoConnector


class MongoObject:
    __connector__ = MongoConnector

    @classmethod
    def _get_name_of_property(cls, property_name):
        _property = cls.properties().get(property_name)
        if not _property:
            raise Exception(f"No Property named '{property_name}' has been found")

        return _property.name

    @classmethod
    def _get_collection(cls):
        collection_name = cls.__collection__
        return cls.__connector__().db[collection_name]

    @classmethod
    def get(cls, _id):
        collection = cls._get_collection()
        item = collection.find_one({"_id": _id})

        if item:
            return cls(item)

    @classmethod
    def find(cls, **kwargs):
        parsed_kwargs = {}
        collection = cls._get_collection()

        for key, value in kwargs.items():
            parsed_kwargs[cls._get_name_of_property(key)] = value

        items = collection.find(parsed_kwargs)
        return [cls(item) for item in items]

    def save(self):
        data = self.to_json()
        collection = self._get_collection()
        collection.update_one({"_id": data['_id']}, {'$set': data}, upsert=True)
        return self
