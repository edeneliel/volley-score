import strawberry
from api.base_query import Query
from api.base_mutation import Mutation

schema = strawberry.Schema(query=Query, mutation=Mutation)
