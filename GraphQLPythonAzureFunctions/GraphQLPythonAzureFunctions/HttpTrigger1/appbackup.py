import azure.functions as func
from ariadne import gql, QueryType
from ariadne import make_executable_schema,load_schema_from_path #,ResolverMap
from ariadne.asgi import GraphQL
from graphql import graphql_sync
import json
from graphql import graphql


def main(req: func.HttpRequest) -> func.HttpResponse:

    type_defs = load_schema_from_path("schema.graphql")

    query = QueryType()
    #query = ResolverMap("Query")

    @query.field("hello")
    def resolve_hello(*_):
        return func.HttpResponse("Hello world new!",status_code=200)


    schema = make_executable_schema(type_defs, query)
    result = graphql(schema, query)
    a = 1
    #result1 = graphql_sync(schema,"""{ hello }""")
    # result = graphql(
    #         schema,
    #         query            
    #     )
    
    #app = GraphQL(schema, debug=True)
    
    #return func.HttpResponse(json.dumps(result1.data),status_code=200)
    return func.HttpResponse(
              "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
              status_code=200
    )
        
