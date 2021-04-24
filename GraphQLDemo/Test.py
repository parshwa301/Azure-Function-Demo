import graphene

import json

class DBAG(graphene.ObjectType):

    id = graphene.String()
    city = graphene.String()
    countryid = graphene.String()

class Query(graphene.ObjectType):

    data = graphene.Field(graphene.List(DBAG))
    def resolve_data(self, info):
        
        x = [{"id": "1","city": "as","countryid": "2"},{"id": "2","city": "aghj","countryid": "8"},{"id": "3","city": "afgh","countryid": "12"}]
        return x

class GraphQLWithModel:
    def __init__(self):
        self.schema = graphene.Schema(
            query=Query
        )
        print(self.schema)

    def graphquery(self, query):
        # results = self.schema.execute(query, middleware=[timing_middleware,AuthorizationMiddleware()]) #authorization_middleware])
        results = self.schema.execute(query)
        return json.dumps(results.data)
