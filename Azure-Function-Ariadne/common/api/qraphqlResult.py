import asyncio
from ariadne import make_executable_schema,load_schema_from_path #,ResolverMap
from ariadne.asgi import GraphQL
from graphql import graphql_sync
from graphql import graphql

class GraphQLResult:

    def __init__(self):
        pass
    
    async def getGraphQLResult(self,schemadetails,operationdetails):
        result =  await graphql(schemadetails, operationdetails)
        return result