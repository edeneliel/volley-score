import strawberry
from flask import Flask
from api.base_query import Query
from api.base_mutation import Mutation
from strawberry.flask.views import GraphQLView

schema = strawberry.Schema(query=Query, mutation=Mutation)

app = Flask(__name__)
app.add_url_rule("/graphql", view_func=GraphQLView.as_view("graphql_view", schema=schema),)


