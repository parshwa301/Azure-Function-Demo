import azure.functions as func
from ariadne import gql, QueryType
from ariadne import make_executable_schema,load_schema_from_path
from ariadne.asgi import GraphQL

def main(req: func.HttpRequest) -> func.HttpResponse:

    type_defs = load_schema_from_path("schema.graphql")

    query = QueryType()

    @query.field("hello")
    def resolve_hello(*_):
        return "Hello world!"


    schema = make_executable_schema(type_defs, query)
    app = GraphQL(schema, debug=True)

    return func.HttpResponse(
              "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
              status_code=200
    )
        
