from ariadne import make_executable_schema
from ariadne.constants import PLAYGROUND_HTML
from ariadne import gql, QueryType
from django.http import (
    HttpResponse, HttpResponseBadRequest, JsonResponse
)
from django.views import View
from graphql import format_error, graphql
from ariadne.asgi import GraphQL

type_defs = """
    type Query {
        hello: String!
    }
"""

query = QueryType()


@query.field("hello")
def resolve_hello(_, info):
    #request = info.context["environ"]
    #user_agent = request.get("HTTP_USER_AGENT", "guest")
    return "Hello, saurabh"


# Create executable schema instance
schema = make_executable_schema(type_defs, query)
app = GraphQL(schema, debug=True)

# Create GraphQL view
class GraphQLView(View):
    # On GET request serve GraphQL Playground
    # You don't need to provide Playground if you don't want to
    # bet keep on mind this will nor prohibit clients from
    # exploring your API using desktop GraphQL Playground app.
    def get(self, request, *args, **kwargs):
        return HttpResponse(PLAYGROUND_HTML)

    # GraphQL queries are always sent as POSTd
    def post(self, request, *args, **kwargs):
        # Reject requests that aren't JSON
        if request.content_type != "application/json":
            return HttpResponseBadRequest()

        # Naively read data from JSON request
        try:
            data = json.loads(request.data)
        except ValueError:
            return HttpResponseBadRequest()

        # Check if instance data is not empty and dict
        if not data or not isinstance(data, dict):
            return HttpResponseBadRequest()

        # Check if variables are dict:
        variables = data.get("variables")
        if variables and not isinstance(variables, dict):
            return HttpResponseBadRequest()

        # Execute the query
        result = graphql(
            schema,
            data.get("query"),
            context_value=request,  # expose request as info.context
            variable_values=data.get("variables"),
            operation_name=data.get("operationName"),
        )

        # Build valid GraphQL API response
        response = {"data": result.data}
        if result.errors:
            response["errors"] = [format_error(e) for e in result.errors]

        

        # Send response to client
        return JsonResponse(response)