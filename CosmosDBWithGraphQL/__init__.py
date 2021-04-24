import logging
import azure.functions as func
from CosmosDBWithGraphQL.GraphQLTest import *


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python HTTP trigger function processed a request.')

    req_body = req.get_json()
    query_string  = req_body.get('query')

    results = GraphQL().query(query_string)

    return func.HttpResponse(
            results,
            status_code=200,
            mimetype="application/json"            
    )
    
