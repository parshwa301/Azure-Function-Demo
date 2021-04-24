import logging

import azure.functions as func
from GraphQLDemo.Test import * 


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python HTTP trigger function processed a request.')

    #query = req.params.get('query')
    req_body = req.get_json()
    query_string  = req_body.get('query')

#     results = GraphQL().query(query_string)

    results = GraphQLQuery().graphquery(query_string)

    return func.HttpResponse(
            results,
            status_code=200,
            mimetype="application/json"            
    )
    

