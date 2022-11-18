import strawberry
from flask import Flask
from api.base_query import Query
from api.base_mutation import Mutation
from strawberry.flask.views import GraphQLView

schema = strawberry.Schema(query=Query, mutation=Mutation)

app = Flask(__name__)
app.add_url_rule("/graphql", view_func=GraphQLView.as_view("graphql_view", schema=schema),)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
