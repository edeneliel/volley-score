import strawberry


@strawberry.type
class PlayerType:
    id: str

    name: str
    number: int
    picture: str
