import os
from azure.cosmos import *

class CosmosDataSet:
    def __init__(self):
        pass

    def dbconnection(self, containerName) -> ContainerProxy:

        url = os.environ['ACCOUNT_EndPoint']
        key = os.environ['Account_Key']
        client = CosmosClient(url, credential=key)
        database_name = 'dbag'
        database = client.get_database_client(database_name)
        container = database.get_container_client(containerName)

        return container