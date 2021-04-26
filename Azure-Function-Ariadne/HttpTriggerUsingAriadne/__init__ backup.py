import azure.functions as func
from ariadne import gql, QueryType
from ariadne import make_executable_schema,load_schema_from_path #,ResolverMap
from ariadne.asgi import GraphQL
from graphql import graphql_sync
import json
from graphql import graphql
import asyncio

async def getGraphQLResult(schemadetails,operationdetails):
    #result =  await graphql(schema1, """{ hello }""")
    result =  await graphql(schemadetails, operationdetails)
    a = 1
    return result

def main(req: func.HttpRequest) -> func.HttpResponse:

    type_defs = load_schema_from_path("schema.graphql")

    query = QueryType()
    #query = ResolverMap("Query")
    
    req_body = req.get_json()
    operationdetails = req_body.get('query')

    @query.field("hello")
    def resolve_hello(*_):
        return "Hello world saurabh!"
    
    @query.field("employee")
    def resolve_employee(*_):
        clean_input = {
        "empid": "189130",
        "empname": "saurabh"
    }
        return clean_input

    schema = make_executable_schema(type_defs, query)
    response = asyncio.run(getGraphQLResult(schema,operationdetails))
    
   
    #app = GraphQL(schema, debug=True)
    
    #return func.HttpResponse(json.dumps(result1.data),status_code=200)
    return func.HttpResponse(
              json.dumps(response.data),
              status_code=200
    )
    #"This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
    

        
