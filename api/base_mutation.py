from typing import List, Union, Any
from strawberry.tools import create_type
from strawberry.field import StrawberryField
from api.mutations.give_point import give_point
from api.mutations.start_game import start_game

mutations: List[Union[StrawberryField, Any]] = [
    give_point,
    start_game
]

Mutation = create_type("Mutation", mutations)