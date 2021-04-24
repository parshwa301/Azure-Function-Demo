import graphene

import json


class Query(graphene.ObjectType):

    # this defines a Field `hello` in our Schema with a single Argument `name`
    hello = graphene.String(name=graphene.String(default_value="stranger"))
    goodbye = graphene.String()

    # our Resolver method takes the GraphQL context (root, info) as well as
    # Argument (name) for the Field and returns data for the query Response
    def resolve_hello(root, info, name):
        return f'Hello {name}!'

    def resolve_goodbye(root, info):
        return 'See ya!' 




class GraphQL:
    def __init__(self):
        self.schema = graphene.Schema(
            query=Query
        )
        print(self.schema)

    def query(self, query):
        # results = self.schema.execute(query, middleware=[timing_middleware,AuthorizationMiddleware()]) #authorization_middleware])
        results = self.schema.execute(query)
        return json.dumps(results.data)

