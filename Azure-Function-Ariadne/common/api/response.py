import azure.functions as func
from ariadne import QueryType
from ariadne import make_executable_schema,load_schema_from_path #,ResolverMap
import json
from graphql import graphql
import asyncio

class ApiResponse:

    def __init__(self):
        pass

    def getApiResponse(self, response):
        result = json.dumps(response.data)
        return result