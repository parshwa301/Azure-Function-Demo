import azure.functions as func
from ariadne import QueryType
from ariadne import make_executable_schema,load_schema_from_path #,ResolverMap
import json
from graphql import graphql
import asyncio
from resolver.firds_resolver import *
from common.api.qraphqlResult import *
from common.api.request import *

def main(req: func.HttpRequest) -> func.HttpResponse:

    type_defs = load_schema_from_path("schema/firds/firds.graphql")

    operationdetails = ApiRequest().getApiRequest(req)

    schema = make_executable_schema(type_defs, query)
    response = asyncio.run(GraphQLResult().getGraphQLResult(schema,operationdetails))
    
    return func.HttpResponse(
              json.dumps(response.data),
              status_code=200
    )

        
