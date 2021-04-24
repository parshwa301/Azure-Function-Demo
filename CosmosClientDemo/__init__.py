import logging
import azure.functions as func
from azure.cosmos import CosmosClient
import os
import json


def main(req: func.HttpRequest) -> func.HttpResponse:

    # pageNo = int(req.params.get('pageNo'))
    # print("hello")
    url = os.environ['ACCOUNT_EndPoint']
    key = os.environ['Account_Key']
    client = CosmosClient(url, credential=key)
    database_name = 'DBAG'
    database = client.get_database_client(database_name)
    container_name = 'FIRDS'
    container = database.get_container_client(container_name)

# Enumerate the returned items
    body={
        "id":"25",
        "city":"ahmedabad",
        "countryid":"67"
    }
    container.create_item(body)

    # items = list(container.query_items(query='SELECT f.id,f.city FROM FIRDS f where f.countryid between 1 and 10 OFFSET @pageNo LIMIT 5',  parameters=[
    #     dict(name='@pageNo', value=pageNo)
    # ],enable_cross_partition_query=True))
    return func.HttpResponse(
            json.dumps(body),
            status_code=200,
            mimetype="application/json"            
    )

        