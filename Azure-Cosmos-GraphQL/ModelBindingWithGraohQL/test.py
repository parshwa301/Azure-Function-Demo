from schema import *

results = GraphQL().graphquery("query_string")

    # return func.HttpResponse(
    #         results,
    #         status_code=200,
    #         mimetype="application/json"            
    # )