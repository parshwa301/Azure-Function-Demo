import graphene
from CosmosDBWithGraphQL.CosmosDBConnection import * 
from azure.cosmos import *
import json


class FIRDS(graphene.ObjectType):

    id = graphene.String()
    city = graphene.String()
    countryid = graphene.String()


class Query(graphene.ObjectType):

    data = graphene.Field(graphene.List(FIRDS))
    def resolve_data(self, info):

        container = CosmosDataSet().dbconnection("FIRDS")
        items = list(container.query_items(query='SELECT * FROM FIRDS',enable_cross_partition_query=True))
        return items

class GraphQL:
    def __init__(self):
        self.schema = graphene.Schema(
            query=Query
        )
        print(self.schema)

    def query(self, query):
      
        results = self.schema.execute(query)
        return json.dumps(results.data)


