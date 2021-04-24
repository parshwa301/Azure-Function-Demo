import graphene
from models.model import *
from query import *
import json


class GraphQL:
    def __init__(self):
        self.schema = graphene.Schema(
            query=Query,
            types=[Firds, Fitrs]
        )
        print(self.schema)

    def graphquery(self, query):
        # results = self.schema.execute(query, middleware=[timing_middleware,AuthorizationMiddleware()]) #authorization_middleware])
        results = self.schema.execute(query)
        return json.dumps(results.data)